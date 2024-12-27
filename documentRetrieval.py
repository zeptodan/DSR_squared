import json
from ranking import rank_similar_words
from utils import FAISS,lexicon,nlp,words,embeddings
def search(query : str):
    words=[]
    doc = nlp(query)  # renamed from 'words' to 'doc'
    for token in doc:  # iterate over spaCy tokens
        wordlemma = token.lemma_
        if wordlemma in lexicon:
            words.append(wordlemma)
    tmpDocs=load_and_rank(words)  
    resultantDocs=[[key,value] for key,value in tmpDocs.items()]
    resultantDocs.sort(key=lambda x:x[1],reverse=True)
    return resultantDocs
        

def load_and_rank(wordtoLoad):
    words_to_doc={}
    barrels={}
    newWords=find_matches(wordtoLoad,5)   
    for newWord in newWords:
        barrel = lexicon[newWord]["barrel"]
        if barrel not in barrels:
            barrels[barrel]=[]
        barrels[barrel].append(newWord)
    for barrel,wordstoLoad in barrels.items():
        load_words_from_barrel(words_to_doc,barrel,wordstoLoad)
    tmpDocs={}
    rank_similar_words(words_to_doc,newWords,lexicon, 4040997,tmpDocs)
    return tmpDocs
        
def load_words_from_barrel(words_to_doc,barrel,wordstoLoad):
    file=open("barrels/barrel-" + barrel + ".json")
    data=json.load(file)
    for word in wordstoLoad:
        words_to_doc[word] = data[lexicon[word]["id"]]
    
    
def find_matches(word, k):


    wordID = lexicon[word]['id']
    
    word_embedding = embeddings[int(wordID)].reshape(1, -1)
    distances, indices = FAISS.search(word_embedding, k)
    matches = {}

    for ID, distance in zip(indices[0], distances[0]):
        print(words[str(ID)]['word'])
        matches[words[str(ID)]['word']] = distance
    print(matches)
    return matches
