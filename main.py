import pandas as pd
import spacy
from documentRetrieval import search
def main():
    lexi = pd.read_csv("Lexicon_small.csv", names=["count", "word", "id"], keep_default_na=False, na_values=[])
    lexicon=lexi.set_index("word").to_dict(orient="index")
    nlp = spacy.load("en_core_web_md")
    query = input("enter: ")
    docs = search(query,lexicon,nlp)
    i=0
    for doc in docs:
        print(doc)
        i+=1
        if i==20:
            break
if __name__ == "__main__":
    main()
        