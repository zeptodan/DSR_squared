import pandas
import faiss
import numpy
import csv


loaded = False
word_count = 0
embeddings = None
FAISS = None
lexicon = {}

def resource_loader():
    global loaded
    
    if not loaded:
        global word_count
        global embeddings
        global FAISS
        global lexicon

        x = pandas.read_csv("Lexicon_small.csv", usecols=[2])
        words= x.iloc[:, 0].tolist()
        word_count = len(words)
        embeddings = numpy.load("vectors.npy")
        FAISS = faiss.read_index("Faiss_index.index")
        with open("LexiconFinal.csv") as f:
            file = csv.reader(f)
            for row in file:
                word = row[1]
                stuff = [int(row[2]), int(row[0])]
                lexicon[word] = stuff
        loaded = True

# Function to find similar words
def find_matches(word, k):
    global word_count
    global words
    global embeddings
    global FAISS
    global lexicon

    wordID = lexicon[word][1]
    if wordID<1 or wordID>word_count:
        return {}

    word_embedding = embeddings[wordID].reshape(1, -1)
    distances, indices = FAISS.search(word_embedding, k)

    matches = {}

    for ID, distance in zip(indices[0], distances[0]):
        matches[words[ID]] = distance
    
    return matches

    """
    # Retrieve similar words and their distances
    similar_words = list(zip([i for i in indices[0]], distances[0]))
    return similar_words
    """