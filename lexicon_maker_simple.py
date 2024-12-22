'''
Takes the dataset and generates a lexicon for each word
wordID, word, doc-count
'''
import pandas as pd
import spacy
import ijson
import os




# Variables
# modify these according to your system and preferences
json_path = r'TheCleanData.json'
csv_path = r'Lexicon.csv'
word_counter_size = 7 #number of digits for the wordID
global word_counter 
word_counter = 1
nlp = spacy.load("en_core_web_md")

#================================================================================
#Main
lexicon = {}
def json_lexicon(json_path):

    doc_counter = 1
    


    # Load JSON file 

    with open(json_path, 'r') as file:
            objects = ijson.items(file, "item")
            # data = json.load(file)
            while True:
                chunk = [obj for _, obj in zip(range(1000), objects)]  
                if not chunk:
                    break   
                df = pd.DataFrame(chunk)   
                for i,obj in df.iterrows():
                    print(f"Processing {doc_counter}")
                    process_doc(obj)
                    doc_counter += 1 
                

    print("Writing to csv")
    write_to_csv()           
         

    #Write the entire lexicon to csv
   

#================================================================================
#Functions


# Process a doc for the lexicon
def process_doc(obj):
    global word_counter 

    master_string = ''

    #extract title, keywords, abstract
    master_string +=(' '+ obj['title'].strip())
    master_string+=(' '+  obj['abstract'].strip())
    master_string +=(' '+  list_to_string(obj['keywords']).strip())

    
    if not master_string: 
        return
    master_string = nlp(master_string.lower())
    #lemmatize and filter words
    unique_words = {token.lemma_ for token in master_string
                if token.is_alpha and not token.is_stop
                and len(token) > 2 and token.text in nlp.vocab}
    for token in unique_words:
        if token not in lexicon:
            lexicon[token] = [word_counter, 1]  # Store ID and count
            word_counter+=1
        else:
            lexicon[token][1] += 1  # Increment count

#write the final lexicon to a .csv file
def write_to_csv():
    if lexicon:  # Proceed only if there are tokens
        df = pd.DataFrame(lexicon.values(), columns=['wordID', 'count'], index=lexicon.keys()).reset_index()
        df.columns = ['word', 'count', 'wordID']  # Rename columns appropriately
        df = df[['wordID', 'word', 'count']] # Reorder columns to ID, word, count
    if not os.path.exists(csv_path):
        # Write with headers if the file doesn't exist
        df.to_csv(csv_path, mode='w', index=False, header=False)
    else:
        # Append without headers if the file exists
        df.to_csv(csv_path, mode='a', index=False, header=False)
        


# Convert a list to a string
def list_to_string(lst):
    if not lst:
        return ''
    return ' '.join(str(s) for s in lst)
    
#Generate a wordID for a new word
# def str_wordID():
#     global word_counter
#     global word_counter_size
#     counter = word_counter
#     numbstr = str(counter)
#     padding = word_counter_size-len(numbstr)
#     returnstr = '0' * padding + numbstr
#     word_counter+=1
#     return returnstr



# Run the script
json_lexicon(json_path)
