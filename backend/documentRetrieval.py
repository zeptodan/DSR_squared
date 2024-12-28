import json
from ranking import rank_similar_words
from utils import FAISS,lexicon,nlp,words,embeddings
import numpy as np
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
    
    
def find_matches(query_words, k, list_of_all_words):
    embeddings - []
    for word in query_words:
        wordID = lexicon[word]['id']
        word_embedding = embeddings[int(wordID)-1].reshape(1, -1)
        embeddings.append(word_embedding)

    whole_distances, whole_indices = FAISS.search(embeddings, k)
    matches = {}

    for matches_indices, matches_distances in zip(whole_distances, whole_indices):
        for ID, distance in zip(matches_indices, matches_distances):
            matches[list_of_all_words[ID]] = distance
    print(matches)
    return matches