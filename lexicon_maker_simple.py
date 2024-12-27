import pandas as pd
import spacy
import ijson
import os
from collections import defaultdict

# Variables
json_path = r'1000_clean_dataset.json'
csv_path = r'Lexicon_small.csv'
current_ID = 1
chunk_size = 10000 

# Load SpaCy with disabled components for speed
nlp = spacy.load("en_core_web_md", disable=['tok2vec', 'tagger', 'parser' , 'attribute_ruler', 'ner'])

# Lexicon storage
lexicon = defaultdict(lambda: [0, 0])  # Default [ID, count]

# Process documents using spaCy's pipe
def process_docs(master_strings):
    global current_ID
    docs = nlp.pipe(master_strings, batch_size=1000, n_process=4)
    
    for doc in docs:
        unique_words = {token.lemma_ for token in doc
                        if token.text.isalnum() and not token.is_stop and token.is_oov}

        for token in unique_words:
            if lexicon[token][0] == 0:
                lexicon[token] = [current_ID, 1]  # Assign new ID
                current_ID += 1
            else:
                lexicon[token][1] += 1  # Increment count

# Write results to CSV
def write_to_csv():
    if lexicon:
        df = pd.DataFrame.from_dict(lexicon, orient='index', columns=['wordID', 'count'])
        df.reset_index(inplace=True)
        df.columns = ['word', 'wordID', 'count']
        df.to_csv(csv_path, index=False, header=False)

# Convert a list to string
def list_to_string(lst):
    if not lst:
        return ''
    return ' '.join(str(s) for s in lst)

# Main JSON processing
def json_lexicon(json_path):
    with open(json_path, 'r') as file:
        objects = ijson.items(file, "item")
        while True:
            chunk = [obj for _, obj in zip(range(chunk_size), objects)]
            if not chunk:
                break

            master_strings = [' '.join([
                obj['title'].strip(),
                obj['abstract'].strip(),
                list_to_string(obj['keywords']).strip()
            ]) for obj in chunk]

            # Process documents in batches using pipe
            process_docs(master_strings)

    # Write final lexicon to CSV
    write_to_csv()

# Run the script
json_lexicon(json_path)
