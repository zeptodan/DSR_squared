import ijson
import json
#function to give score to words in the document based on its importance
def calculate_weight(value,length):
    return (value["T"]+value["K"]+value["A"])/length
    

file = open("Forward_index.json","r")
writefile=open("Inverted_index.json","w")
documents=ijson.items(file,"item")
inverted_index={}
i=1
#iterate over the forward index
for document in documents:
    print("processing " + str(i))
    i+=1
    DocID=document["id"]
    offset=document["off"]
    #iterate over the key value pairs in the document
    for key,value in document.items():
        #ignore if it is not a word id
        if key not in ["id","authors","cite","len","off","url"]:
            #if the word is not in inverted index
            #for each word store list of document id, its weight and documents offset in forward index
            if key not in inverted_index:
                inverted_index[key]=[[DocID,calculate_weight(value,document["len"]),offset]]
            #if it is already there just append the list of documents where that word appears
            else:
                inverted_index[key].append([DocID,calculate_weight(value,document["len"]),offset])
json.dump(inverted_index,writefile,separators=(',',':'))