# DSR<sup>2</sup>
## A Delectable Succulent Research Retrieval Search Engine
DSR<sup>2</sup> is a search engine for research paper.
# Dataset
The [Massive Scholarly Dataset]([(https://www.kaggle.com/search)]) was taken and filtered to make it according to our requirements. The dataset originallly contained 5M+ records and the columns where:
0.   id                  
1.   title               
2.   doi                   
3.   issue                
4.   keywords            
5.   lang                 
6.   venue                
7.   year                 
8.   n_citation           
9.   page_start           
10.  page_end             
11.  volume
12.  issn
13.  isbn
14.  url
15.  abstract
16.  authors
17.  doc_type
18.  references
19.  fos
20.  indexed_abstract
21.  v12_id
22.  v12_authors

Articles that lacked a URL, had both keywords and abstract missing, or were not in English were dropped, leaving 4,040,997 articles. The remaining columns were:

0.   id
1.   title
2.   keywords
3.   lang
4.   year
5.   n_citation
6.   url
7.   abstract
8.   authors

