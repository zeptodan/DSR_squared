import pandas
import faiss
import hdbscan
import spacy
import numpy
from sklearn.preprocessing import normalize
import gc


#FILENAMES
lexi = "LexiconFinal.csv"
spacy_model = "en_core_web_md"
new_lexi = "Clusters.csv"

########################################################
print("Loading model")
nlp = spacy.load(spacy_model)
print("Loaded model\n")

print("Loading lexicon")
Lexicon = pandas.read_csv(lexi, usecols=[1, 2])
print("Loaded lexicon\n")

print("Extracting words")
#extract words
words= Lexicon.iloc[:, 0]
print("Extracted words\n")

#Generate a list of vectors
vectors = []
vector_count = 1
print("Generating vectors:")
for word in words:
    if vector_count%100 == 0:
        print(f"{vector_count}")
    vectors.append(nlp(str(word)).vector)
    gc.collect()
    vector_count+=1

del nlp

print("\n\n\nCasting to numpy array:")
vectors = numpy.array(vectors)
vectors = vectors.astype(numpy.float32)

print("\nNormalizing")
vectors = normalize(vectors, norm='l2')

#Reduce the dimensions of the embeddings using PCA in FAISS (originally 300)
print("\n\nUsing PCA to reduce dimensionality")
pca_matrix = faiss.PCAMatrix(300, 50)
pca_matrix.train(vectors)
embeddings = pca_matrix.apply_py(vectors)

#Generate cluster labels for each word(vector)
print("\nUsing DBSCAN\n")
algo = hdbscan.HDBSCAN(min_cluster_size=3, metric='cosine', prediction_data=True)
clusters = algo.fit_predict(embeddings)

#Append the cluster labels to the lexicon
print("Writing to file")
Lexicon['Clusters'] = clusters
Lexicon.to_csv(new_lexi, header = ['Words', 'ID', 'Clusters'], index=False)