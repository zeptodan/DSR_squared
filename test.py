import spacy
import faiss
import numpy as np

# Load spaCy model
nlp = spacy.load('en_core_web_md')

# Example lexicon and embeddings (replace with your actual data)
lexicon = {
    'example': {'id': 0},
    'test': {'id': 1},
    'word': {'id': 2}
}
words = {
    '0': 'example',
    '1': 'test',
    '2': 'word'
}
embeddings = np.array([
    nlp('example').vector,
    nlp('test').vector,
    nlp('word').vector
])

# Create a FAISS index and add embeddings
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def find_matches(word, k):
    # Get word embedding using spaCy
    doc = nlp(word)
    word_embedding = doc.vector.reshape(1, -1)

    # Perform a search
    distances, indices = index.search(word_embedding, k)
    matches = {}

    for ID, distance in zip(indices[0], distances[0]):
        matches[words[str(ID)]] = distance
    
    return matches

# Example usage
word = "example"
k = 2
matches = find_matches(word, k)
print(matches)

# with multiprocessing.Manager() as manager:
#     shared_dict=manager.dict()
#     for barrel,wordstoLoad in barrels.items():
#         process = multiprocessing.Process(target=load_words_from_barrel(shared_dict,barrel,wordstoLoad))
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()