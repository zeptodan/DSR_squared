import math
from multiprocessing import Pool


def rank_single_word(word ,docs,similarity, lexicon, total_docs):
    local_resultant_docs={}
    doc_count=lexicon[word][1]
    idf=math.log(total_docs/doc_count)

    min_citations = min(doc[1] for doc in docs)
    max_citations = max(doc[1] for doc in docs)
    if(min_citations==max_citations):
        no_cit=True
    normalized_citations=0
    for doc in docs:
        if not no_cit:
            normalized_citations=(doc[1]-min_citations)/(max_citations-min_citations)
        score=((idf*doc[1])*similarity+normalized_citations)
        local_resultant_docs[doc[0]]=score      

    return local_resultant_docs

def rank_similar_words(words_and_docs, similarity, lexicon, total_docs):
    resultant_docs={}
    args=[(word,docs,similarity[word],lexicon,TOTAL_DOCS) for word,docs in words_and_docs.items()]
    with Pool() as pool:
        results=pool.starmap(rank_single_word,args)
    combine_results(results)

def combine_results(results):    
    for local_resultant_docs in results:
        for doc_id, score in local_resultant_docs.items():
            if doc_id in resultant_docs:
                resultant_docs[doc_id] += 1
            else:
                resultant_docs[doc_id] = score

    print(resultant_docs)
    return resultant_docs
def main():
    global lexicon, words_and_docs, TOTAL_DOCS, similarity,resultant_docs

    lexicon={'hello':(0,2),'world':(1,3),'python':(2,4)}
    words_and_docs={'hello':[[0,1,12]],'world':[[1,.5,2]]}
    TOTAL_DOCS=4040997
    resultant_docs={}
    similarity={'hello':0.5,'world':1,'python':3}

    rank_similar_words(words_and_docs, similarity, lexicon, TOTAL_DOCS)
if __name__ == '__main__':
    main()