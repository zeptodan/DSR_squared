import math
def rank_similar_words(words_and_docs, similarity, lexicon, total_docs,resultant_docs):
    print("nnnn")
    for word,docs in words_and_docs.items():
        doc_count=lexicon[word]['count']
        idf=math.log(total_docs/doc_count)
        for doc in docs:
            score=((idf*doc[1])*similarity[word])
            if doc[0] in resultant_docs:
                resultant_docs[doc[0]] += score
            else:
                resultant_docs[doc[0]] = score

# def main():
#     global lexicon, words_and_docs, TOTAL_DOCS, similarity,resultant_docs
#     lexicon={'hello':(0,2),'world':(1,3),'python':(2,4)}
#     words_and_docs={'hello':[[69,1,12]],'world':[[70,.5,2]]}
#     TOTAL_DOCS=4040997
#     resultant_docs={}

#     similarity={'hello':1,'world':2,'python':3}
#     print(resultant_docs)

# if __name__ == '__main__':
#     main()