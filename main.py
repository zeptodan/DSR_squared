import pandas as pd
import spacy
from documentRetrieval import search
import time
dataset=r"TheCleanData"
def main():
    lexi = pd.read_csv("Lexi_clusters.csv", names=["count", "word", "id","barrel"],dtype={"count":int, "word":str, "id":str,"barrel":str}, keep_default_na=False, na_values=[])
    lexicon=lexi.set_index("word").to_dict(orient="index")
    nlp = spacy.load("en_core_web_md")
    query = input("enter: ")
    start = time.time()
    docs_to_load = search(query,lexicon,nlp)
    print("time for whole search: " + str(time.time() - start))
    docs=getDocs(docs_to_load)
        
def getDocs(docs_to_load):
    start = time.time()
    stack=[]
    docs=[]
    i=0
    with open(dataset+".json","r") as file:
        for document in docs_to_load:
            doc="{"
            stack.clear()
            file.seek(document[0])
            stack.append(file.read(1))
            while len(stack) !=0:
                doc+=file.read(1)
                if doc[-1] == "{":
                    stack.append("{")
                elif doc[-1] == "}":
                    stack.pop()
            docs.append(doc)
            i+=1
            if i==10:
                break
    print("getting docs from dataset: " + str(time.time() - start))
    return docs
        
        
if __name__ == "__main__":
    main()
        