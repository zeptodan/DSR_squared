import utils
import multiprocessing
import json
#from ranking import sas
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
        #combine()
        #getDocs(offsets)
        

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
    #docs= rank(newWords,words_to_doc)
        
def load_words_from_barrel(words_to_doc,barrel,wordstoLoad):
    file=open("barrels/barrel-" + str(barrel) + ".json")
    data=json.load(file)
    for word in wordstoLoad:
        words_to_doc[word] = data[word]
    
    
def getDocs(offsets):
    print("TODO")


# with multiprocessing.Manager() as manager:
#     shared_dict=manager.dict()
#     for barrel,wordstoLoad in barrels.items():
#         process = multiprocessing.Process(target=load_words_from_barrel(shared_dict,barrel,wordstoLoad))
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()