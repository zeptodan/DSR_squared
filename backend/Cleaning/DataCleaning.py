import json
import pandas as pd
import ijson
import os
# cleaning the data
def clean_DataChuncks(df):
    
    # coulumns to be dropped
    columns_to_drop=['fos','indexed_abstract','v12_id','v12_authors','doi','issue','issn','isbn','page_start','page_end','volume','doc_type','venue','references']
    df.drop(columns=columns_to_drop,inplace=True,errors='ignore')
    count_records=0
    # Dropping the records that don't have any url or the records that don't have both the keywords and abstract of lang!=en
    for index,current in  df.iterrows():
        if(current['url']==[] or (current['keywords']==[] and current['abstract']=='') or current['lang']!='en'):
            df.drop(index,inplace=True)
            

    count_records=len(df)    
    df = df.to_dict('records')
    append_to_json('TheCleanData2.0.json',df)
    return count_records
# storing the clean dara
def append_to_json(file_path, new_record):
    # Check if the file exists
    file_exists = os.path.exists(file_path)
    offset=[]
    # Open the file in r+ read mode if it doesn't exist open in w mode
    with open(file_path, "r+" if file_exists else "w") as file:
        if not file_exists or os.path.getsize(file_path) == 0:  
            file.write("[")
            for i,record in enumerate(new_record):
                offset.append(file.tell())
                json.dump(record, file)
                if i<len(new_record)-1:
                    file.write(",")
            file.write("]")
        else:
            # File exists: Append to it
            file.seek(0, os.SEEK_END)  # Move to the end of the file
            file.seek(file.tell() - 1, os.SEEK_SET)  # Move back 1 character to overwrite the closing bracket "]"
            file.write(",")
            for record in new_record:
                offset.append(file.tell())
                json.dump(record, file)
                file.write(",")
            file.seek(0, os.SEEK_END)  # Move to the end of the file
            file.seek(file.tell() - 1, os.SEEK_SET)  
            file.write("]")

    df=pd.DataFrame(offset)
    csv_path='offsets.csv'
    if not os.path.exists(csv_path):
        # Write with headers if the file doesn't exist
        df.to_csv(csv_path, mode='w', index=False, header=False)
    else:
        # Append without headers if the file exists
        df.to_csv(csv_path, mode='a', index=False, header=False)
file_path = r"TheCleanData.json"
with open(file_path, "r") as file:
    count=0
    objects = ijson.items(file, "item")
    # go through the data in form of chunks without loading the whole file
    while(True):
        chunk = [obj for _, obj in zip(range(20000), objects)]  
        if not chunk:
            break   
        df = pd.DataFrame(chunk)   
        count+=clean_DataChuncks(df)
        print(count)
print(count)


# After droping columns
#  0   id             object
#  1   title          object
#  2   keywords    l  object
#  3   lang           object
#  4   year           int64
#  5   n_citation     int64
#  6   url            object
#  7   abstract       object
#  8   authors        object

# Original data

#  0   id                   object
#  1   title                object
#  2   doi                  object     drop
#  3   issue                object     drop
#  4   keywords             object     keywords==[]
#  5   lang                 object     Drop other than en
#  6   venue                object     Drop (where the article is published)
#  7   year                 int64      
#  8   n_citation            int64      
#  9   page_start            object     drop
#  10  page_end              object     drop
#  11  volume                object     drop
#  12  issn                  object     drop
#  13  isbn                  object     drop
#  14  url                   object     url==[]
#  15  abstract              object     abstract==''
#  16  authors               object     
#  17  doc_type              object     drop
#  18  references            object     drop
#  19  fos                   object     drop
#  20  indexed_abstract      object     drop
#  21  v12_id                float64    drop
#  22  v12_authors           object     drop