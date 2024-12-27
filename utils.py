import pandas
import faiss
import numpy
import spacy
#loading lexicon and embeddings
lexi = pandas.read_csv("Lexi_clusters.csv", names=["count", "word", "id","barrel"],dtype={"count":int, "word":str, "id":str,"barrel":str}, keep_default_na=False, na_values=[])
lexicon=lexi.set_index("word").to_dict(orient="index")
nlp = spacy.load("en_core_web_md")
words= lexi.set_index("id").to_dict(orient="index")
embeddings = numpy.load("vectors.npy")
FAISS = faiss.read_index("Faiss_index.index")
