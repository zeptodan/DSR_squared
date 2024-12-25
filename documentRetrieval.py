import utils
import multiprocessing
import json
from ranking import rank_similar_words,combine_results
def search(query : str,lexi,nlp):
    words=nlp.load(query)
    processes=[]
    with multiprocessing.Manager() as manager:
        shared_list=manager.list()
        for word in words:
            wordlemma = word.lemma_
            if wordlemma in lexi:
                process = multiprocessing.Process(target=load_and_rank(shared_list,wordlemma,lexi))
                processes.append(process)
                process.start()
        for process in processes:
            processes.join()
        tmpDocs=combine_results(shared_list)
        resultantDocs=list(tmpDocs)
        resultantDocs.sort()
        return resultantDocs
        

def load_and_rank(wordtoLoad,shared_list,lexi):
    words_to_doc={}
    barrels={}
    newWords = utils.find_matches(wordtoLoad,5,lexi)    
    for newWord in newWords:
        barrel = lexi[newWord]["barrel"]
        if barrel not in barrels:
            barrels[barrel]=[]
        barrels[barrel].append(newWord)
    for barrel,wordstoLoad in barrels.items():
        load_words_from_barrel(words_to_doc,barrel,wordstoLoad)
    
    shared_list.append(rank_similar_words(words_to_doc,newWords,lexi, 4040997))
        
def load_words_from_barrel(words_to_doc,barrel,wordstoLoad):
    file=open("barrels/barrel-" + str(barrel) + ".json")
    data=json.load(file)
    for word in wordstoLoad:
        words_to_doc[word] = data[word]
    
    


# with multiprocessing.Manager() as manager:
#     shared_dict=manager.dict()
#     for barrel,wordstoLoad in barrels.items():
#         process = multiprocessing.Process(target=load_words_from_barrel(shared_dict,barrel,wordstoLoad))
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()