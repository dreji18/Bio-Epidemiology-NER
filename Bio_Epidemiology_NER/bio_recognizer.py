# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:19:28 2022

@author: dreji18
"""

# loading the packages
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
import fitz

import nltk
nltk.download('punkt')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
from nltk.tokenize import word_tokenize

# loading the biomedical ner model
tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

# dictionary of common diseases
disease_list = ['covid', 'covid19', 'covid-19', 'coronavirus', 'corona virus', 'long covid', 'long-covid', 'post-covid', 'post covid']


#%%
def load_model(compute):
    # pass device=0 if using gpu
    if compute == 'gpu':
        pipe = pipeline("ner",
                        model=model,
                        tokenizer=tokenizer,
                        aggregation_strategy="max",
                        device=0)
    else:
        pipe = pipeline("ner",
                        model=model,
                        tokenizer=tokenizer,
                        aggregation_strategy="max")
     
    return pipe

# function to perform ner on text corpus
def ner_prediction(corpus, compute):

    pipe = load_model(compute)
    
    master_df = pd.DataFrame()
    for sentence in sent_tokenizer.tokenize(corpus):
        pred = pipe(sentence)
    
        pred_df = pd.DataFrame(pred)

        tokenized_sentence = word_tokenize(sentence)
        
        actuall_values_list = []
        for i in range(len(pred_df)):
            pred_text = sentence[pred_df['start'].iloc[i]: pred_df['end'].iloc[i]]
            try:       
                tokenized_pred_text = word_tokenize(pred_text)   
                actual_collection = []
                for i in tokenized_pred_text:
                    for j in tokenized_sentence:
                        if i in j:
                            actual_collection.append(j)
                
                actual_word = ' '.join(actual_collection)
            except:
                actual_word = pred_text
                continue
            
            actuall_values_list.append(actual_word)
            

        pred_df['value'] = actuall_values_list
        
        # checking whether any diseases are missed with disease list
        disease_extraction = []
        for i in disease_list:
            for j in tokenized_sentence:
                if i.lower() in j.strip().lower():
                    disease_extraction.append(j)
                    
        disease_extraction = list(set(disease_extraction))
        disease_df = pd.DataFrame(disease_extraction, columns = ['value'])
        disease_df['score'] = 1
        disease_df['entity_group'] = 'Disease_disorder'
        
        # only if there are predictions for a sentence 
        if len(pred_df) != 0:
            final_df = pred_df[['entity_group', 'value', 'score']]
            
            final_df = final_df.append(disease_df) # adding the disease_df to existing
            
            # final_df = final_df.drop_duplicates(
            #   subset = ['entity_group', 'value'],
            #   keep = 'first')

            master_df = master_df.append(final_df)
            
            master_df = master_df.drop_duplicates(
              subset = ['entity_group', 'value'],
              keep = 'first').reset_index(drop=True)
        
    return master_df

# function to extract entities from pdf's and annotate
def pdf_annotate(pdffile,compute, output_format='all'):
    try:
        file_data = fitz.open(pdffile)
        page = 0
        final_df = pd.DataFrame(columns= ["Page","Entity Group","Value","Score"])
        #to iterate through every page of the pdf
        while page <  file_data.page_count:
            page_text=file_data.get_page_text(page)
            out = ner_prediction(corpus=page_text, compute=compute)
            output = out.drop_duplicates(subset=["value"],keep='first')
            #to iterate through every row in the dataframe
            for index, row in output.iterrows():  
                text = row['value']
                #selecting values which has threshold greater than 0.5
                #avoiding words less than than length of 3 to avoid false positives
                if row["score"] > 0.5 and len(text) > 2:
                    final_df.loc[len(final_df.index)] = [page +1 ,row['entity_group'],row['value'],row['score']] 
                    if output_format in ["pdf",'all']:
                        text_instances = file_data[page].search_for(text)
                        current_page = file_data[page]
                        if text_instances is not None:
                            #for adding/marking the annotation in the pdf
                            for inst in text_instances:
                                #coordinates of the annoation in the pdf
                                x0,x1,x2,x3 = inst
                                rect = (x0,x1,x2,x3)
                                annot = current_page.add_rect_annot(rect) 
                                info = annot.info
                                info["title"]   = row['entity_group']
                                annot.set_info(info)
                                annot.update()
                    
                                
            page+=1  
        
        if len(final_df)!=0:
            final_df['Pdf File'] = pdffile
            final_df = final_df[['Entity Group', 'Value', 'Score', 'Page', 'Pdf File']]
        else:
            print("No Entities Extracted!!!")
        
        if output_format in ["pdf",'all']:                              
            file_data.save(pdffile.replace(".pdf", "_annot.pdf"))   
        if output_format in ["csv",'all']:    
            final_df.to_csv(pdffile.replace(".pdf", "_df.csv"))
        return final_df
    except Exception as e:
          print("Error occured: {}".format(e))
          raise e      

















