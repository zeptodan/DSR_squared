import pandas as pd
import spacy

##Path to json
json = 'json.json'

####################################################
nlp = spacy.load("en_core_web_lg")
set = {}
dataframe = pd.DataFrame({})

def json_lexicon(json):
    meta = pd.read_json(json, lines = True)
    titlelist = meta[title].tolist()
    abstractlist = meta[abstract].tolist()
    keywordslist = meta[keywords].tolist()

    titles = list_to_string(titlelist)
    abstracts = list_to_string(abstractlist)
    keywordss = listlist_to_string(keywordslist)

    add_to_set(titles)
    add_to_set(abstracts)
    add_to_set(keywordss)

    append_vectors(set)
    
    dataframe.to_csv(index=False)


#uprocess a title, keyword, paragraph
def add_to_set(paragraph):
    data = paragraph.lower()
    tokkens = [token.lemma_ for token in data
               if not token.is_stop and token.is_alpha]
    for tokken in tokkens:
        set.add(tokken)
    

#word2vec
def vector(tokken):
    return nlp(tokken).vector

def append_vectors(set):
    tuples = [(word, vector(word)) for word in set]
    df = pd.DataFrame(tuples)
    dataframe.append(df)

def list_to_string(list):
    s = ' '.join(str(s) for s in list)
    return s

def listlist_to_string(list):
    s = '\n'.join([' '.join(map(str, sublist)) for sublist in list])
    return s



