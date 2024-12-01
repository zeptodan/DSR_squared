import pandas as pd
import ijson
import spacy
import json
#load lexicon as dictionary
lexi=pd.read_csv("Lexicon.csv",names=["count","word","id"])
lexicon=lexi.set_index("word").to_dict(orient="index")
#open dataset file and file to write in
file=open("1000_clean_dataset.json","r")
writefile=open("Forward_index.json","w")
documents=ijson.items(file,"item")
nlp = spacy.load("en_core_web_md")
document_index={}
i=1
count=0
writefile.write("[")
for document in documents:
    print("processing " + str(i))
    count=0
    if i!=1:
        writefile.write(",")
    document_index["id"]=document["id"]
    document_index["off"]=writefile.tell()
    document_index["cite"]=document["n_citation"]
    document_index["url"]=document["url"]
    authors=[author["name"] for author in document["authors"]]
    document_index["authors"]=authors
    i+=1
    title=nlp(''.join(document["title"]))
    count+=len(title)
    for word in title:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":1,"K":0,"A":0}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["T"]+=1
            
    keywords=nlp(''.join(document["keywords"]))
    count+=len(keywords)
    for word in keywords:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":0,"K":1,"A":0}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["K"]+=1
            
    abstract=nlp(''.join(document["abstract"])) 
    count+=len(abstract)
    for word in abstract:
        wordlemma=word.lemma_.lower()
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":0,"K":0,"A":1}
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["A"]+=1
    document_index["len"]=count
    json.dump(document_index,writefile,separators=(',',':'))
    document_index.clear()
writefile.write("]")
writefile.close()
file.close()
    