import ijson
import json
#function to give score to words in the document based on its importance
def calculate_weight(value,length):
    return (value[0]+value[1]+value[2])/length
    
offsets=open("offsets.csv","r")
offsetlist=offsets.readlines()
offsetlist=[int(offset) for offset in offsetlist]
file = open("Forward_index.json","r")
writefile=open("Inverted_index.json","w")
documents=ijson.items(file,"item")
inverted_index={}
i=0
#iterate over the forward index
for document in documents:
    offset=offsetlist[i]
    i+=1
    print("processing " + str(i))
    #iterate over the key value pairs in the document
    for key,value in document.items():
        #ignore if it is not a word id
        if key !="L":
            #if the word is not in inverted index
            #for each word store list of document id, its weight and documents offset in forward index
            if key not in inverted_index:
                inverted_index[key]=[[calculate_weight(value,document["L"]),offset]]
            #if it is already there just append the list of documents where that word appears
            else:
                inverted_index[key].append([calculate_weight(value,document["L"]),offset])
                
json.dump(inverted_index,writefile,separators=[",",":"])