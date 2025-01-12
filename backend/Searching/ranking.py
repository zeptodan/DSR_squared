import math
def rank_similar_words(words_and_docs, similarity, lexicon, total_docs,resultant_docs):
    for word,docs in words_and_docs.items():
        doc_count=lexicon[word]['count']
        idf=math.log(total_docs/doc_count)
        for doc in docs:
            if doc[2]==100000000:
                print(doc)
            score=((idf*float(doc[1]))*pow(similarity[word],3))+doc[2]
            if doc[0] in resultant_docs:
                resultant_docs[doc[0]] += 10*score
            else:
                resultant_docs[doc[0]] = score


