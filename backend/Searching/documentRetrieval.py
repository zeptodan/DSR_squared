import json
from ranking import rank_similar_words
from utils import FAISS,lexicon,nlp,words,embeddings
import numpy as np
from collections import defaultdict
def search(query : str):
    words=[]
    doc = nlp(query)  # renamed from 'words' to 'doc'
    for token in doc:  # iterate over spaCy tokens
        wordlemma = token.lemma_
        if wordlemma in lexicon:
            words.append(wordlemma)
    tmpDocs=load_and_rank(words)  
    resultantDocs = sorted(tmpDocs.items(), key=lambda x: x[1], reverse=True)
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
        if barrel:
            load_words_from_barrel(words_to_doc,barrel,wordstoLoad)
    tmpDocs=defaultdict(int)
    rank_similar_words(words_to_doc,newWords,lexicon, 4040997,tmpDocs)
    return tmpDocs
        
def load_words_from_barrel(words_to_doc,barrel,wordstoLoad):
    file=open("D:\\DSR_squared\\backend\\barrels\\barrel-" + barrel + ".json")
    data=json.load(file)
    
    for word in wordstoLoad:
        words_to_doc[word] = data[lexicon[word]["id"]]
    
    
def find_matches(query_words, k):
    matches = {}
    currentEmbedding=[]
    for word in query_words:
        matches[word]=1
        if word not in lexicon:
            continue  # Skip this word if it's not found
        wordID = int(lexicon[word]['id'])-1
        word_embedding = embeddings[wordID].reshape(1, -1)
        currentEmbedding.append(word_embedding)
    
    if currentEmbedding == []:
        return matches
    query_embeddings = np.vstack(currentEmbedding)
    whole_distances, whole_indices = FAISS.search(query_embeddings, k)

    for matches_distances, matches_indices in zip(whole_distances, whole_indices):
        for ID, distance in zip(matches_indices, matches_distances):
            word_id = str(ID + 1)
            if word_id in words:
                matches[words[word_id]["word"]] = distance
    return matches
