Bio-Epidemiology-NER is an Python library built on top of biomedical-ner-all model to recognize bio-medical entities from a corpus or a medical report

[![Downloads](https://static.pepy.tech/personalized-badge/bio-epidemiology-ner?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/bio-epidemiology-ner)
<a href="https://pypi.org/project/Bio-Epidemiology-NER/">
    <img alt="CI" src="https://img.shields.io/badge/pypi-v0.1.3-orange">
</a>
<a href="https://youtu.be/rYJOpUVWszY">
    <img alt="CI" src="https://img.shields.io/badge/Demo-Video-red">
</a>
<a href="https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000152">
    <img alt="CI" src="https://img.shields.io/badge/Research-Paper-green">
</a>

| Feature  | Output  |
|---|---|
| Named Entity Recognition | Recognize 84 bio-medical entities |
| PDF Input | Read Pdf and tabulate the entities|
| PDF Annotation | Annotate Entities in a medical pdf report|

## Tutorial
[<img src="https://github.com/dreji18/Bio-Epidemiology-NER/blob/main/output/thumbnail.png" width="50%">](https://youtu.be/xpiDPdBpS18 "Watch the video")

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Bio-Epidemiology-NER

```bash
pip install Bio-Epidemiology-NER
```

This package has dependency over Pytorch, please install the required configuration from this link https://pytorch.org/get-started/locally/

## Usage

## NER with Bio-Epidemiology-NER
```python
# load all the functions
from Bio_Epidemiology_NER.bio_recognizer import ner_prediction

# returns the predicted class along with the probability of the actual EnvBert model
doc = """
	CASE: A 28-year-old previously healthy man presented with a 6-week history of palpitations. 
      The symptoms occurred during rest, 2–3 times per week, lasted up to 30 minutes at a time 
      and were associated with dyspnea. Except for a grade 2/6 holosystolic tricuspid regurgitation 
      murmur (best heard at the left sternal border with inspiratory accentuation), physical 
      examination yielded unremarkable findings.
      """

# returns a dataframe output
ner_prediction(corpus=doc, compute='cpu') #pass compute='gpu' if using gpu

```

## Annotate the entities in a Medical Report and export as pdf/csv format 
```python
# load all the functions
from Bio_Epidemiology_NER.bio_recognizer import pdf_annotate

# enter pdf file name
pdffile = 'Alhashash-2020-Emergency surgical management.pdf'

# returns a annotated pdf file
pdf_annotate(pdffile,compute='cpu', output_format='pdf') #pass compute='gpu' if using gpu

# returns a csv file with entities
pdf_annotate(pdffile,compute='cpu', output_format='csv') #pass compute='gpu' if using gpu

# return both annotated pdf and csv file
pdf_annotate(pdffile,compute='cpu', output_format='all') #pass compute='gpu' if using gpu

```


## About the Model
The model within this package is an English Named Entity Recognition model, trained on Maccrobat to recognize the bio-medical entities (84 entities) from a given text corpus (case reports etc.). This model was built on top of distilbert-base-uncased

- Dataset : Maccrobat https://figshare.com/articles/dataset/MACCROBAT2018/9764942
- Carbon emission : 0.0279399890043426 Kg
- Training time : 30.16527 minute
- GPU used : 1 x GeForce RTX 3060 Laptop GPU

for more details regarding the entities supported, check the config file https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json

## Ownership & License
This Package is part of the Research topic "AI in Biomedical field" conducted by Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset),

Please cite us [**Research Paper**](https://github.com/dreji18/Bio-Epidemiology-NER/blob/main/CITATION.cff) 

and star at: https://github.com/dreji18/biomedicalNER

[MIT](https://choosealicense.com/licenses/mit/) License
