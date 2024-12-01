import ijson
import json

def calculate_weight(value,length):
    return (value["T"]+value["K"]+value["A"])/length
    

file = open("Forward_index.json","r")
writefile=open("Inverted_index.json","w")
documents=ijson.items(file,"item")
inverted_index={}
i=1
for document in documents:
    print("processing " + str(i))
    i+=1
    DocID=document["id"]
    offset=document["off"]
    for key,value in document.items():
        if key not in ["id","authors","cite","len","off","url"]:
            if key not in inverted_index:
                inverted_index[key]=[[DocID,calculate_weight(value,document["len"]),offset]]
            else:
                inverted_index[key].append([DocID,calculate_weight(value,document["len"]),offset])
json.dump(inverted_index,writefile,separators=(',',':'))