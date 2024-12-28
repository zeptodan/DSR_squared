import pandas as pd
import ijson
from tqdm.notebook import tqdm
import spacy
from collections import defaultdict

# Variables
json_path = r'/content/drive/MyDrive/DSRsquared/Clean_Dataset_Large.json'
csv_path = r'LexiconFull.csv'
chunk_size = 10000



# Load SpaCy with disabled components for speed
print("Loading model")
nlp = spacy.load("en_core_web_md", disable=['tok2vec', 'parser', 'ner'])

lexicon = defaultdict(lambda: [0, 0])  # Default [ID, count]
current_ID = 1

# Process documents using spaCy's pipe
def process_docs(master_strings):
    global current_ID, lexicon
    docs = nlp.pipe(master_strings, batch_size=200, n_process=1)
    for doc in docs:
        unique_words = set(token.lemma_ for token in doc
                        if token.text.isalnum() and not token.is_stop
                           and not token.is_oov)

        for word in unique_words:

            if lexicon[word][0] == 0:
                lexicon[word] = [current_ID, 1]  # Assign new ID
                current_ID += 1
            else:
                lexicon[word][1] += 1  # Increment count

# Write results to CSV
def write_to_csv(lexicon):
    if lexicon:
        df = pd.DataFrame.from_dict(lexicon, orient='index', columns=['wordID', 'count'])
        df.reset_index(inplace=True)
        df.columns = ['word', 'wordID', 'count']
        df.to_csv(csv_path, index=False, header=False)

# Convert list or set to string
def to_string(iterable):
    return ' '.join(str(s) for s in iterable) if iterable else ''

# Process JSON and build lexicon
def json_lexicon(json_path):
    with open(json_path, 'r') as file:
        objects = ijson.items(file, "item")
        pbar = tqdm(total=1000000, desc='Processing docs: ')
        doc_counter = chunk_size

        while(True):
            chunk = [obj for _, obj in zip(range(chunk_size), objects)]
            if not chunk:
                break
            elif doc_counter >=1000000:
                break

            # Prepare strings
            master_strings = [' '.join([
            obj['title'].strip(),
            obj['abstract'].strip(),
            to_string(obj['keywords']).strip()
            ]) for obj in chunk]
            del chunk
                
            # Process documents
            process_docs(master_strings)
            doc_counter += chunk_size
            # Cleanup
            del master_strings
            pbar.update(chunk_size)

        pbar.close()

    # Write final lexicon
    write_to_csv(lexicon)

if __name__ == "__main__":
    json_lexicon(json_path)

