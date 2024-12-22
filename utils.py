import pandas
import faiss
import numpy

Lexicon = pandas.read_csv("Lexicon.csv", usecols=[2])
words= Lexicon.iloc[:, 0].tolist()
word_count = len(words)
embeddings = numpy.load(".\\semantic\\vectors.npy")
FAISS = faiss.read_index(".\\semantic\\Faiss_index.index")

# Function to find similar words
def find_matches(wordID, k):
    if wordID<0 or wordID>word_count:
        return []

    word_embedding = embeddings[wordID].reshape(1, -1)
    _, indices = FAISS.search(word_embedding, k)

    # Retrieve similar words and their distances
    similar_words = list(indices[0])
    return similar_words