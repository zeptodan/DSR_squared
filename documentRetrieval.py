import utils
import multiprocessing
import json
import time
from ranking import rank_similar_words,combine_results
def search(query : str,lexi,nlp):
    words=nlp(query)
    processes=[]
    start = time.time()
    with multiprocessing.Manager() as manager:
        shared_list=manager.list()
        for word in words:
            wordlemma = word.lemma_
            if wordlemma in lexi:
                process = multiprocessing.Process(target=load_and_rank,args=(wordlemma,shared_list,lexi))
                processes.append(process)
                process.start()
        print("multiprocessing creation: " + str(time.time()-start))
        for process in processes:
            process.join()
        tmpDocs=combine_results(shared_list)
        resultantDocs=[[key,value] for key,value in tmpDocs.items()]
        resultantDocs.sort(key=lambda x:x[1],reverse=True)
        return resultantDocs
        

def load_and_rank(wordtoLoad,shared_list,lexi):
    words_to_doc={}
    barrels={}
    newWords = {wordtoLoad: 1}#utils.find_matches(wordtoLoad,5,lexi)    
    for newWord in newWords:
        barrel = lexi[newWord]["barrel"]
        if barrel not in barrels:
            barrels[barrel]=[]
        barrels[barrel].append(newWord)
    for barrel,wordstoLoad in barrels.items():
        load_words_from_barrel(words_to_doc,barrel,wordstoLoad,lexi)
    
    shared_list.append(rank_similar_words(words_to_doc,newWords,lexi, 4040997))
        
def load_words_from_barrel(words_to_doc,barrel,wordstoLoad,lexi):
    file=open("barrels/barrel-" + barrel + ".json")
    data=json.load(file)
    for word in wordstoLoad:
        words_to_doc[word] = data[lexi[word]["id"]]
    
    


# with multiprocessing.Manager() as manager:
#     shared_dict=manager.dict()
#     for barrel,wordstoLoad in barrels.items():
#         process = multiprocessing.Process(target=load_words_from_barrel(shared_dict,barrel,wordstoLoad))
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()