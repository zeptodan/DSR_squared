import pandas as pd
import csv
import ijson
import pickle
lexi = pd.read_csv("Lexicon_1_Mill.csv", names=["word", "id", "count"], keep_default_na=False, na_values=[])
lexicon=lexi.set_index("id").to_dict(orient="index")
file1=open("Inverted_index_copy.json","r")
i=0
count=0
path=r"backend/pickled_barrels/barrel-"
file=open(path+"0" + ".pkl","wb")
cluster={}
for key,value in  ijson.kvitems(file1, ''):
    if i %100==0:
        print("barrel" + str(i) +"done")
    if count ==10:
        i+=1
        count=0
        pickle.dump(cluster,file)
        cluster.clear()
        file.close()
        file=open(path+str(i) + ".pkl","wb")
    count+=1
    cluster[key] = value
    lexicon[int(key)]["cluster"] = i
if cluster:
    pickle.dump(cluster,file)
with open("lexi_clusters.csv", mode="w", newline="",encoding="UTF-8") as file:
    writer = csv.writer(file)
    for key, value in lexicon.items():
        if "cluster" in value:
            writer.writerow([value["word"], key,value["count"],value["cluster"]])
        else:
            print(value)
            writer.writerow([value["word"], key,value["count"]])