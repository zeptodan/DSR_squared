import math
from multiprocessing import Pool
import time

def rank_single_word(word ,docs,similarity, lexicon, total_docs):
    local_resultant_docs={}
    doc_count=lexicon[word]["count"]
    idf=math.log(total_docs/doc_count)
    no_cit=False
    min_citations = min(doc[2] for doc in docs)
    max_citations = max(doc[2] for doc in docs)
    if(min_citations==max_citations):
        no_cit=True
    normalized_citations=0
    for doc in docs:
        if not no_cit:
            normalized_citations=(doc[2]-min_citations)/(max_citations-min_citations)
        score=((idf*doc[1])*similarity+normalized_citations)
        local_resultant_docs[doc[0]]=score      

    return local_resultant_docs

def rank_similar_words(words_and_docs, similarity, lexicon, total_docs):
    start = time.time()
    resultant_docs={}
    args=[(word,docs,similarity[word],lexicon,total_docs) for word,docs in words_and_docs.items()]
    with Pool() as pool:
        results=pool.starmap(rank_single_word,args)
    resultant_docs=combine_results(results)
    print("ranking time: " + str(time.time() - start))
    return resultant_docs

def combine_results(results):    
    resultant_docs={}
    for local_resultant_docs in results:
        for doc_id, score in local_resultant_docs.items():
            if doc_id in resultant_docs:
                resultant_docs[doc_id] += score
            else:
                resultant_docs[doc_id] = score
    return resultant_docs
def main():
    global lexicon, words_and_docs, TOTAL_DOCS, similarity,resultant_docs

    lexicon={'hello':(0,2),'world':(1,3),'python':(2,4)}
    words_and_docs={'hello':[[69,1,12]],'world':[[70,.5,2]]}
    TOTAL_DOCS=4040997
    resultant_docs={}
    similarity={'hello':0.5,'world':1,'python':3}

    rank_similar_words(words_and_docs, similarity, lexicon, TOTAL_DOCS)
if __name__ == '__main__':
    main()