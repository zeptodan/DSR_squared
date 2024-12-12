import pandas
import faiss
import hdbscan
import spacy
import numpy


#FILENAMES
lexi = "LexiconFinal.csv"
spacy_model = "en_core_web_md"
new_lexi = 'Clusters.csv'

########################################################
nlp = spacy.load(spacy_model)
Lexicon = pandas.read_csv(lexi, usecols=[1, 2])

#convert the dataframe to a list of words
words= pandas.read_csv(lexi, usecols=[1]).squeeze().tolist()

#Generate a list of vectors
vectors = numpy.array([nlp(word).vector for word in words])
vectors = vectors.astype(numpy.float32)

#Reduce the dimensions of the embeddings using PCA in FAISS (originally 300)
pca_matrix = faiss.PCAMatrix(300, 50)
pca_matrix.train(vectors)
embeddings = pca_matrix.apply_py(vectors)

#Generate cluster labels for each word(vector)
algo = hdbscan.HDBSCAN(min_cluster_size=3, metric='cosine', prediction_data=True)
clusters = algo.fit_predict(embeddings)

#Append the cluster labels to the lexicon
Lexicon['Clusters'] = clusters
Lexicon.to_csv(new_lexi, header = ['Words', 'ID', 'Clusters'], index=False)