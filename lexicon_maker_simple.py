import pandas as pd
import json
import spacy

# Variables
json_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\1000_clean.json'
csv_path = 'D:\\Danish\\Study\\NUST\\Data Structures and Algorithms\\Project\\DSR_squared\\LexiconSimple2.csv'
chunk_size = 100
word_counter_size = 7
nlp = spacy.load("en_core_web_sm")

#================================================================================
#Main
lexicon = {}
def json_lexicon(json_path):
    lexicon
    doc_counter = 1
    global word_counter
    word_counter = 1

    # Load JSON file 
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)

        for obj in data:
            print(f"Processing {doc_counter}")
            process_doc(obj)
            doc_counter += 1

    except Exception as e:
        print(f"An error occurred while processing JSON: {e}")

    #Write the entire lexicon to csv
    print("Writing to csv")
    write_to_csv()

#================================================================================
#Functions


# Process a doc for the lexicon
def process_doc(obj):
    global lexicon
    master_string = ''

    #extract title, keywords, abstract
    if 'title' in obj and obj['title']:
        master_string +=(' '+ obj['title'])
    if 'abstract' in obj and obj['abstract']:
        master_string+=(' '+  obj['abstract'])
    if 'keywords' in obj and obj['keywords']:
        master_string +=(' '+  list_to_string(obj['keywords']))

    
    if not master_string: 
        return
    master_string = nlp(master_string.lower())
    unique_words = {token.lemma_ for token in master_string
             if not token.is_stop and token.is_alpha 
             and all(ord(char) < 128 for char in token.text)
             and not len(token)<=2}
    unique_words = list(unique_words)
    for token in unique_words:
        if token not in lexicon:
            lexicon[token] = [str_wordID(), 1]  # Store ID and count
        else:
            lexicon[token][1] += 1  # Increment count


def write_to_csv():
    global lexicon
    if lexicon:  # Proceed only if there are tokens
        df = pd.DataFrame(lexicon.values(), columns=['wordID', 'count'], index=lexicon.keys()).reset_index()
        df.columns = ['word', 'count', 'wordID']  # Rename columns appropriately
        df = df[['wordID', 'word', 'count']]  # Reorder columns to ID, word, count
        df.to_csv(csv_path, header=False, index=False)


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
    padding = word_counter_size-len(numbstr)
    returnstr = '0' * padding + numbstr
    word_counter+=1
    return returnstr



# Run the script
json_lexicon(json_path)
