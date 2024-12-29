import pandas as pd
import os
import json
import ijson
from tqdm import tqdm

df = pd.read_csv("Lexicon_1_Barrels.csv", usecols=[1, 3],names=["ID","Cluster"])
Barrels = dict(zip(df['ID'], df['Cluster']))
file1=open("inverted_index_third.json","r")
print("The Might index has loaded")
for index_str, value in tqdm(ijson.kvitems(file1, ''), desc="Index: "):
    index = int(index_str)
    # Get the barrel (cluster) for this index
    barrel = Barrels.get(index)
    if barrel is None:
        print(f"Warning: No barrel found for index {index}")
        continue
    barrel_file = f"backend\\barrels\\barrel-{barrel}.json"
    if not os.path.exists(barrel_file):
        with open(barrel_file, 'w') as file:
            json.dump({index_str: value}, file, separators=(',',':'))
    else:
        with open(barrel_file, 'r+') as file:
            try:
                data = json.load(file)
                data[index_str] = value  
                file.seek(0)
                json.dump(data, file, separators=(',',':'))
                file.truncate()
            except json.JSONDecodeError:
                file.seek(0)
                json.dump({index_str: value}, file, separators=(',',':'))