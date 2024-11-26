import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def tokelemma(text):
    data = text.lower()
    tokkens = [token.lemma_ for token in data
               if not token.is_stop and token.is_alpha]
    return tokkens

def vectorize (tokens)
    for token in tokens:

