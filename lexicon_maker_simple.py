import pandas as pd
import spacy

# Variables
json_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\1000_clean.json'
csv_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\LexiconSimple.csv'
chunk_size = 100
word_counter_size = 7
nlp = spacy.load("en_core_web_md")

#================================================================================
#Main
lexicon = pd.DataFrame(columns = ['wordID', 'word', 'count'])
def json_lexicon(json_path):
    doc_counter = 1
    global word_counter
    word_counter = 1

    # Load JSON file 
    for chunk in pd.read_json(json_path):
        for obj in chunk:
            print(f"Processing {doc_counter}")
            # Check and process each field
            if 'title' in obj and obj['title']:
                add_to_lexicon(obj['title'])
            if 'abstract' in obj and obj['abstract']:
                add_to_lexicon(obj['abstract'])
            if 'keywords' in obj and obj['keywords']:
                add_to_lexicon(list_to_string(obj['keywords']))
            
            doc_counter += 1

    #Write the entire lexicon to csv
    print("Writing to csv")
    write_to_csv()

#================================================================================
#Functions


# Process a string for the lexicon
def add_to_lexicon(string):
    if not string or len(string.strip()) < 2:  # Avoid very short strings
        return
    data = nlp(string.lower())
    tokens = [token.lemma_ for token in data
             if not token.is_stop and token.is_alpha 
             and all(ord(char) < 128 for char in token.text)]
    for token in tokens:
        if token not in lexicon['word'].values:
            lexicon.loc[len(lexicon)] = [str_wordID, token, 1]
        elif token in lexicon['word'].values:
            lexicon.loc[lexicon['word'] == token, 'count']+=1


def write_to_csv():
    global lexicon
    if len(lexicon)>0:  # Proceed only if there are tokens
        lexicon.to_csv(csv_path, header=False, index=False)

# Convert a list to a string
def list_to_string(lst):
    if not lst:
        return ''
    return ' '.join(str(s) for s in lst)

def str_wordID():
    global word_counter
    global word_counter_size
    counter = word_counter
    numbstr = str(counter)
    padding = word_counter_size-numbstr.size()
    returnstr = 0*padding + numbstr
    word_counter+=1
    return returnstr



# Run the script
json_lexicon(json_path)
