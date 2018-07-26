# Speyside: pretrained spaCy models by NLP Town

This is a repository of NLP models trained by NLP Town. If you need custom 
models, get in touch through [our website](http://www.nlp.town).

![Made with spaCy](img/made%20with%20%25E2%259D%25A4%20and-spaCy-09a3d5.svg)

| Model name    | Size  | Description |
| ------------- |-------| ------------|
| [en_sentiment_reviews_md](https://github.com/nlptown/speyside/releases/download/0.0.0/en_sentiment_reviews_sm-2.0.0.tar.gz)      | 22MB  | Sentiment classification trained on 3.6M Amazon reviews. |

## Usage

### Installation

Install the models using pip: 

```
pip install MODEL_URL
```

You can consult the metadata of a model like this: 

```
python -m spacy info en_sentiment_reviews_sm
```

### Classification

```
>>> import spacy
>>> nlp = spacy.load("en_sentiment_reviews_sm")
>>> nlp("This is a horrible movie").cats
{'positive': 0.0016374080441892147, 'negative': 0.9983626008033752}
>>> nlp("This is a great movie").cats
{'positive': 0.995779275894165, 'negative': 0.004220753442496061}
```