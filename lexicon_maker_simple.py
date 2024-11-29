import modin.pandas as pd
import json
import spacy

# Variables
json_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\1000_clean.json'
csv_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\LexiconSimple.csv'
batch_size = 100

#================================================================================
# Global Variables
nlp = spacy.load("en_core_web_md")
lexicon_set = set()

def json_lexicon(json_path):
    counter = 1

    # Load JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    for obj in data:
        print(f"Tokenizing {counter}")

        # Check and process each field
        if 'title' in obj and obj['title']:
            add_to_set(obj['title'])
        if 'abstract' in obj and obj['abstract']:
            add_to_set(obj['abstract'])
        if 'keywords' in obj and obj['keywords']:
            add_to_set(list_to_string(obj['keywords']))
        
        counter += 1

        # Write to CSV periodically
        if counter % batch_size == 0:
            print(f"Writing batch ending at {counter}")
            set_to_csv()

    # Final write for remaining tokens
    print("Writing final batch")
    set_to_csv()

# Process a string for the set
def add_to_set(string):
    if not string or len(string.strip()) < 2:  # Avoid very short strings
        return
    data = nlp(string.lower())
    tokens = [token.lemma_ for token in data if not token.is_stop and token.is_alpha]
    lexicon_set.update(tokens)

# Append tokens to a CSV file incrementally
def set_to_csv():
    global lexicon_set
    if lexicon_set:  # Proceed only if there are tokens
        df = pd.DataFrame({'Words': list(lexicon_set)})  # Create a DataFrame
        df.to_csv(csv_path, mode='a', header=False, index=False)
        lexicon_set.clear()  # Clear the set for the next batch

# Convert a list to a string
def list_to_string(lst):
    if not lst:
        return ''
    return ' '.join(str(s) for s in lst)

# Run the script
json_lexicon(json_path)
