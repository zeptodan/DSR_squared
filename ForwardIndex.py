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
    global lexicon
    dict = {}
    process_title (dict,doc['title'])

def process_title(dict, title):
    title_words = [token.lemma_ for token in title
                    if not token.is_stop and token.is_alpha
                    and token in lexicon]