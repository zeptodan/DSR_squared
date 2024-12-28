import pandas as pd
import spacy
import ijson
from collections import defaultdict
from tqdm import tqdm




# Variables
json_path = r'TheCleanData2.0.json'
csv_path = r'Lexicon_1m.csv'
current_ID = 1
chunk_size = 1000

# Load SpaCy with disabled components for speed
print("Loading model")
nlp = spacy.load("en_core_web_md", disable=['tok2vec', 'parser', 'ner'])

# Lexicon storage
lexicon = defaultdict(lambda: [0, 0])  # Default [ID, count]

# Process documents using spaCy's pipe
def process_docs(master_strings):
    global current_ID
    docs = nlp.pipe(master_strings, batch_size=200, n_process=1)
    
    for doc in docs:
        unique_words = {token.lemma_ for token in doc
                        if token.text.isalnum() and not token.is_stop and not token.is_oov}

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

        pbar = tqdm(total=1000000, desc='Processing docs: ')

        for i in range(1000):
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
            del(master_strings)
            pbar.update(chunk_size)

    # Write final lexicon to CSV
    write_to_csv()

# Run the script
json_lexicon(json_path)
