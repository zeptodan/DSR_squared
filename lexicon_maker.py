import pandas as pd
import spacy

nlp = spacy.load("en_core_web_lg")
set = {}

def process_to_set(paragraph):
    data = paragraph.lower()
    tokkens = [token.lemma_ for token in data
               if not token.is_stop and token.is_alpha]
    for tokken in tokkens:
        set.add(tokken)

def vector(tokken):

    embedding = nlp(tokken)
    return embedding.vector

        
