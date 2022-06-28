Bio-Epidemiology-NER is an Python library built on top of [biomedical-ner-all model](https://huggingface.co/d4data/biomedical-ner-all)  to recognize bio-medical entities from a corpus or a medical report

| Feature  | Output  |
|---|---|
| Named Entity Recognition | Recognize 84 bio-medical entities |
| PDF Support | feature coming soon...|


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
ner_prediction(corpus=doc, compute='gpu') #pass compute='cpu' if using cpu

```


## About
This model is part of the Research topic "AI in Biomedical and epidemiology field" conducted by Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset),

Please cite us and star at: https://github.com/dreji18/biomedicalNER

## License
[MIT](https://choosealicense.com/licenses/mit/) License
