import pandas as pd
import json
import csv
import ijson
from decimal import Decimal
def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
lexi = pd.read_csv("Lexicon_1_Mill.csv", names=["word", "id", "count"], keep_default_na=False, na_values=[])
lexicon=lexi.set_index("id").to_dict(orient="index")
file1=open("inverted_index_third.json","r")
i=0
count=0
path=r"backend/barrels/barrel-"
file=open(path+"0" + ".json","w")
cluster={}
for key,value in  ijson.kvitems(file1, ''):
    if i %100==0:
        print("barrel" + str(i) +"done")
    if count ==20:
        i+=1
        count=0
        json.dump(cluster,file,separators=[',',':'],default=decimal_serializer)
        cluster.clear()
        file.close()
        file=open(path+str(i) + ".json","w")
    count+=1
    cluster[key] = value
    lexicon[int(key)]["cluster"] = i
if cluster:
    json.dump(cluster,file,separators=[',',':'])
with open("lexi_clusters.csv", mode="w", newline="",encoding="UTF-8") as file:
    writer = csv.writer(file)
    for key, value in lexicon.items():
        if "cluster" in value:
            writer.writerow([value["word"], key,value["count"],value["cluster"]])
        else:
            print(value)
            writer.writerow([value["word"], key,value["count"]])