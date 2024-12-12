import pandas
import faiss
import hdbscan
import spacy


#FILENAMES
lexi = "LexiconFinal.csv"
spacy_model = "en_core_web_md"

########################################################
nlp = spacy.load(spacy_model)
Lexicon = pandas.read_csv(lexi, usecols=[1, 2])
words = pandas.read_csv(lexi, usecols=[1])

