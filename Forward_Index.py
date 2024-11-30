import pandas as pd
import ijson
import spacy
import json
import os
#load lexicon as dictionary
lexi=pd.read_csv("Lexicon.csv",names=["id","word","count"])
lexicon=lexi.set_index("word").to_dict(orient="index")
#open dataset file and file to write in
file=open("1000_clean_dataset.json","r")
writefile=open("Forward_index.json","r+")
documents=ijson.items(file,"item")
nlp = spacy.load("en_core_web_md")
document_index={}
i=1
pos=0
writefile.write("[\n")
for document in documents:
    if i!=1:
        writefile.write(",")
    document_index["DocID"]=i
    i+=1
    title=nlp(''.join(document["title"]))
    for word in title:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"title":1,"keywords":0,"abstract":0}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["title"]+=1
            
    keywords=nlp(''.join(document["keywords"]))
    for word in keywords:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"title":0,"keywords":1,"abstract":0}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["keywords"]+=1
            
    abstract=nlp(''.join(document["abstract"])) 
    for word in abstract:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"title":0,"keywords":0,"abstract":1}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["abstract"]+=1
            
    json.dump(document_index,writefile,indent=4)
    document_index.clear()
writefile.write(" \n]")
writefile.close()
file.close()
    