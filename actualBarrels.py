import pandas as pd
import json
import csv
lexi = pd.read_csv("Lexicon_small.csv", names=["count", "word", "id"], keep_default_na=False, na_values=[])
lexicon=lexi.set_index("id").to_dict(orient="index")
file=open("inverted_index.json","r")
words=json.load(file)
file.close()
i=0
count=0
path=r"barrels/barrel-"
file=open(path+"0" + ".json","w")
cluster={}
for key,value in words.items():
    if count ==20:
        i+=1
        count=0
        json.dump(cluster,file,indent=4)
        cluster.clear()
        file.close()
        file=open(path+str(i) + ".json","w")
    count+=1
    cluster[key] = value
    lexicon[int(key)]["cluster"] = i
if cluster:
    json.dump(cluster,file,indent=4)
with open("lexi_clusters.csv", mode="w", newline="",encoding="UTF-8") as file:
    writer = csv.writer(file)
    for key, value in lexicon.items():
        if "cluster" in value:
            writer.writerow([value["count"], value["word"],key,value["cluster"]])
        else:
            print(value)
            writer.writerow([value["count"], value["word"],key])