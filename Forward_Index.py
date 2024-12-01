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
#iterate over each document in dataset
for document in documents:
    print("processing " + str(i))
    count=0
    if i!=1:
        writefile.write(",")
    #store metadata of document
    #data stored in the forward index will be id,offset,citations,url,authors names as a list ,
    # and words as a dictionary with keys T(title), K(keywords) and A(abstract) with counts for each
    document_index["id"]=document["id"]
    document_index["off"]=writefile.tell()
    document_index["cite"]=document["n_citation"]
    document_index["url"]=document["url"]
    authors=[author["name"] for author in document["authors"]]
    document_index["authors"]=authors
    i+=1
    #iterate over words in title
    title=nlp(''.join(document["title"]))
    count+=len(title)
    for word in title:
        wordlemma=word.lemma_.lower()
        #if word is not in document_index add it
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":1,"K":0,"A":0}
        #otherwise if it is already there increment its count by 1
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["T"]+=1
            
    #iterate over words in keywords
    keywords=nlp(''.join(document["keywords"]))
    count+=len(keywords)
    for word in keywords:
        wordlemma=word.lemma_.lower()
        #if word is not in document_index
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":0,"K":1,"A":0}
        #otherwise if it is already there increment its count by 1
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["K"]+=1
            
    #iterate over words in abstract
    abstract=nlp(''.join(document["abstract"])) 
    count+=len(abstract)
    for word in abstract:
        wordlemma=word.lemma_.lower()
        #if word is not in document_index
        if wordlemma in lexicon and lexicon[wordlemma]["id"] not in document_index:
            document_index[lexicon[wordlemma]["id"]] = {"T":0,"K":0,"A":1}
        #otherwise if it is already there increment its count by 1
        elif wordlemma in lexicon:
            document_index[lexicon[wordlemma]["id"]]["A"]+=1
    document_index["len"]=count
    #write the index created for the document in file
    json.dump(document_index,writefile,separators=(',',':'))
    #clear the index for the next document
    document_index.clear()
#close the list and then the files
writefile.write("]")
writefile.close()
file.close()
    