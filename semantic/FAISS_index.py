import pandas
import numpy
from sentence_transformers import SentenceTransformer
import faiss


#FILENAMES
lexi = "LexiconFinal.csv"
########################################################
print("Loading model")
model = SentenceTransformer('multi-qa-mpnet-base-cos-v1')
Lexicon = pandas.read_csv(lexi, usecols=[1])
words= Lexicon.iloc[:, 0].tolist()

#extract embeddings
vectors = model.encode(words, convert_to_numpy=True).astype("float32")
pca_matrix = faiss.PCAMatrix(vectors.shape[1], 100)
pca_matrix.train(vectors)
numpy.save("vectors.npy", vectors)


embeddings = numpy.load("vectors.npy")

# Normalize embeddings
#faiss.normalize_L2(embeddings)

# Create FAISS index:
"""
GPU index
gpu_res = faiss.StandardGpuResources()
index_cpu = faiss.IndexFlatIP(embeddings.shape[1])
FAISS = faiss.index_cpu_to_gpu(gpu_res, 0, index_cpu)
FAISS.add(embeddings)
"""
FAISS = faiss.IndexFlatIP(embeddings.shape[1])
FAISS.add(embeddings)

# Write the index to file
"""if gpu FAISS:
faiss.write_index(faiss.index_gpu_to_cpu(FAISS), "FAISS index.index")
"""
faiss.write_index(FAISS, "FAISS_index.index")



