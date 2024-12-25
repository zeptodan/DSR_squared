import pandas as pd
import spacy
import ijson
import os
nlp = spacy.load("en_core_web_md")

master_string="We discuss hardware extensions to 3D-texturing units, which are very small but nevertheless remove some substantial performance limits typically found when using a 3D-texturing unit for volume rendering. The underlying algorithm uses only a slight mod$cation of existing method, which limits negative impacts on application software. In particular, the method speeds up the compositing operation, improves texture cache eflciency and allows for early ray termination and empty space skipping. Early ray termination can not be used in the traditional approach. Simulations show that, depending on data set properties, the performance of readily available, low-cost PC graphics accelerators is already suflcient for real-time volume visualization. Thus, in terms ofperformance, the TRIANGLECASTER-extensions can make dedicated volume rendering accelerators unnecessary."
master_string = nlp(master_string.lower())
for token in master_string:
    if token.text in nlp.vocab:
        print(token.text)
ali={token.lemma_ for token in master_string
                if token.is_alpha and not token.is_stop
                and len(token) > 2 and token.text in nlp.vocab}
print(ali)