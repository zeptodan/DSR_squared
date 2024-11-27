import pandas as pd
import json
import spacy

##Paths
json_path = '1000_clean.json'
csv_path = 'Lexicon.csv'

####################################################
nlp = spacy.load("en_core_web_lg")
set = ()
dataframe = pd.DataFrame({})

def json_lexicon(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)

    for obj in data:
        add_to_set(data.get('title'))
        add_to_set(data.get('abstract'))
        add_to_set(list_to_string(data.get('keywords')))

    append_vectors(set)
    dataframe.sort_values(by = 'Word', inplace=True)
    dataframe.to_csv(csv_path, header = False, index=False)


#process a title, keyword, paragraph
def add_to_set(string):
    data = nlp(string.lower())
    tokkens = [tokken.lemma_ for tokken in data
               if not tokken.is_stop and tokken.is_alpha]
    for tokken in tokkens:
        set.add(tokken)
    

#word2vec
def vector(tokken: str):
    return nlp(tokken).vector

def append_vectors(set):
    tuples = [(word, vector(word)) for word in set]
    df = pd.DataFrame(tuples, columns = ['Words', 'Vectors'])
    dataframe = df

def list_to_string(list):
    s = ' '.join(str(s) for s in list)
    return s