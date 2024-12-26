from documentRetrieval import search
import time
import json
dataset=r"TheCleanData2.0"

def main():
    # resource_loader()
    query = input("enter: ")
    start = time.time()
    docs_to_load = search(query)
    docs=getDocs(docs_to_load)
    print("top result: ")
    docs = [json.loads(doc) for doc in docs]
    for doc in docs:
        print(f'The title is {doc['title']}')
        print(f'The keywords is {doc['keywords']}')
        print(doc["abstract"])
        print("\n--------------------------------------")

    print("time for whole search: " + str(time.time() - start))

def getDocs(docs_to_load):
    stack=[]
    docs=[]
    i=0
    with open(dataset+".json","r") as file:
        for document in docs_to_load:
            doc="{"
            stack.clear()
            file.seek(document[0])
            stack.append(file.read(1))
            while len(stack) !=0:
                doc+=file.read(1)
                if doc[-1] == "{":
                    stack.append("{")
                elif doc[-1] == "}":
                    stack.pop()
            docs.append(doc)
            i+=1
            if i==10:
                break
    return docs
        
          
 
if __name__ == "__main__":
    main()
        