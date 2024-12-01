import pandas as pd
import csv 
import json
import spacy

# Variables
dataset_path = '1000_clean.json'
lexicon_path = 'Lexicon.csv'
output_path = 'InvertedIndex.json'
nlp = spacy.load("en_core_web_sm")

################################## MAIN ########################################
ForwardIndex = {}

#load the lexicon as a dictionary
with open(lexicon_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    lexicon = {row[1]: [row[0], row[2]] for row in reader}


#process each document
def process_dataset(dataset_path):
    doc_counter = 1
    try:
        with open(dataset_path, 'r') as file:
            data = json.load(file)

        for obj in data:
            print(f"Processing {doc_counter}")
            process_doc(obj)

    except Exception as e:
        print(f"An error occurred while processing JSON: {e}")



############################### FUNCTIONS #######################################
def process_doc (doc):
    global ForwardIndex
    global lexicon
    dict = {}
    if doc['title']:
        process_title (dict,doc['title'])
    if doc['abstract']:
        process_abstract(dict, doc['abstract'])
    if doc['keywords']:
        process_keywords(dict, doc['keywords'])
    
    #add constructed index to FOrward Index
    ForwardIndex[doc['id']] = dict


def process_title(dict, title):
    global lexicon
    word_counter = 1
    title_words = [token.lemma_ for token in title
                    if not token.is_stop and token.is_alpha
                    and token in lexicon]
    title_ids = [lexicon[word][0] for word in title_words]

    for id in title_ids:
        if id in dict:
            dict['Title'].append(word_counter)
            word_counter+=1
        else:
            dict[str(id)]['Title'] = [word_counter]
            word_counter+=1
    
def process_abstract(dict, abstract):
    word_counter = 1
    global lexicon

    abstract_words = [token.lemma_ for token in abstract
                    if not token.is_stop and token.is_alpha
                    and token in lexicon]
    abstract_ids = [lexicon[word][0] for word in abstract_words]

    for id in abstract_ids:
        if id in dict:
            dict['Abstract'].append(word_counter)
            word_counter+=1
        else:
            dict[str(id)]['Abstract'] = [word_counter]
            word_counter+=1
    
def process_keywords(dict, keywords):
    word_counter = 1
    global lexicon
    keywords_words = list_to_string(keywords)

    keywords_words = [token.lemma_ for token in keywords
                    if not token.is_stop and token.is_alpha
                    and token in lexicon]
    keywords_ids = [lexicon[word][0] for word in keywords_words]

    for id in keywords_ids:
        if id in dict:
            dict['Keywords'].append(word_counter)
            word_counter+=1
        else:
            dict[str(id)]['Keywords'] = [word_counter]
            word_counter+=1


    
# Convert a list to a string
def list_to_string(lst):
    if not lst:
        return ''
    return ' '.join(str(s) for s in lst)

