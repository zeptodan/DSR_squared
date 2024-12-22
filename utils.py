import pandas
import faiss
import numpy


loaded = False
word_count = 0
embeddings = None

# Function to find similar words
def find_matches(wordID, k):
    global loaded
    global word_count
    global embeddings

    if not loaded:
        Lexicon = pandas.read_csv("Lexicon.csv", usecols=[2])
        words= Lexicon.iloc[:, 0].tolist()
        word_count = len(words)
        embeddings = numpy.load(".\\semantic\\vectors.npy")
        FAISS = faiss.read_index(".\\semantic\\Faiss_index.index")
        loaded = True
    
    if wordID<0 or wordID>word_count:
        return []

    word_embedding = embeddings[wordID].reshape(1, -1)
    distances, indices = FAISS.search(word_embedding, k)

    # Retrieve similar words and their distances
    similar_words = list(zip([i for i in indices[0]], distances[0]))
    return similar_words