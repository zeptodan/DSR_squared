import json
from utils import nlp,lexicon
from Inverted_Index import calculate_weight
def docAdd(doc):
    file = open("TheCleanData2.0.json","a")
    offset=file.tell()
    json.dump(doc,file,separators=[",",":"])
    
    count=0
    titlecount=doc["title"].count(" ") +1
    abstractcount=doc["abstract"].count(" ")+1
    Stringkeywords=' '.join(doc["keywords"]).lower().strip()
    keywordcount=Stringkeywords.count(" ")+1
    count+=titlecount+keywordcount+abstractcount
    
    master_string=nlp(doc["title"].lower().strip()+" "+doc["abstract"].lower().strip()+" "+Stringkeywords)
    
    document_index={}
    for word in master_string:
        if word.is_punct:
            continue
        wordlemma=word.lemma_
        #if word is not in document_index add it
        if titlecount >0:
            if wordlemma in lexicon and wordlemma not in document_index:
                document_index[wordlemma] = [1,0,0]
            #otherwise if it is already there increment its count by 1
            elif wordlemma in lexicon:
                document_index[wordlemma][0]+=1
            titlecount-=1
        elif abstractcount >0:
            if wordlemma in lexicon and wordlemma not in document_index:
                document_index[wordlemma] = [0,0,1]
            #otherwise if it is already there increment its count by 1
            elif wordlemma in lexicon:
                document_index[wordlemma][2]+=1
            abstractcount-=1
        else:
            if wordlemma in lexicon and wordlemma not in document_index:
                document_index[wordlemma] = [0,1,0]
            #otherwise if it is already there increment its count by 1
            elif wordlemma in lexicon:
                document_index[wordlemma][1]+=1
    document_index["L"]=count
    document_index["cite"]=doc["n_citation"]
    
    
    
    for key,value in document_index.items():
        if key !="L" and key != "cite":
            file=open("barrels/barrel-" + lexicon[key]["barrel"] + ".json","r")
            invertedbarrel=json.load(file)
            invertedbarrel[lexicon[key]["id"]].append([offset,calculate_weight(value,document_index["L"]),document_index["cite"]])
            file.close()
            file=open("barrels/barrel-" + lexicon[key]["barrel"] + ".json","w")
            json.dump(invertedbarrel,file,separators=[",",":"])
            file.close()
    