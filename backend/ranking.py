import math
def rank_similar_words(words_and_docs, similarity, lexicon, total_docs,resultant_docs):
    for word,docs in words_and_docs.items():
        doc_count=lexicon[word]['count']
        idf=math.log(total_docs/doc_count)
        for doc in docs:
            score=((idf*doc[1])*similarity[word])
            if doc[0] in resultant_docs:
                resultant_docs[doc[0]] += score
            else:
                resultant_docs[doc[0]] = score

