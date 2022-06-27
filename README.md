# Bio_Epidemiology_NER - Recognizing bio-medical entities from a text corpus

Bio_Epidemiology_NER is an Python library built on top of biomedical-ner-all model to recognize bio-medical entities from a corpus or a medical report

[![Downloads](https://static.pepy.tech/personalized-badge/dbias?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/biomedicalner)

| Feature  | Output  |
|---|---|
| Named Entity Recognition | Recognize 84 bio-medical entities |
| PDF Support | feature coming soon...|

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Bio-Epidemiology-NER

```bash
pip install Bio-Epidemiology-NER
```

## Usage

### NER with Bio-Epidemiology-NER
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


## Author
This model is part of the Research topic "AI in Biomedical field" conducted by Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset),

Please cite us and star at: https://github.com/dreji18/biomedicalNER

## License
[MIT](https://choosealicense.com/licenses/mit/) License
