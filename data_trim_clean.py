#to increase speed using parallel processing
#install modin using -->pip install modin[ray]
#then use -->import modin.pandas as pd

import pandas as pd


data = pd.read_json('OriginalDataset', lines=True)

#remove unwanted columns
data.drop(columns = ['doi', 'issue', 'lang', 'venue', 'page_start',
                     'page_end', 'volume', 'issn', 'isbn', 'doc_type',
                     'references', 'fos', 'indexed_abstract', 'v12_id', 'v12_authors'], inplace=True)

#remove rows with null and empty cells
data.dropna(inplace=True)
data = data[data.apply(lambda row: all(len(val) > 0 if isinstance(val, list) else True for val in row), axis=1)]

#function to trim the "authors" value to just the names
def clean_authors(authors):
    # Iterate over each author and remove unwanted keys
    for author in authors:
        author.pop("id", None)  # Remove 'id' if exists
        author.pop("org", None)  # Remove 'org' if exists
    return authors

data['authors'] = data['authors'].apply(clean_authors)

#function to convert the name: "name" pair to a list of author names
def convert_authors_to_list(authors):
    # Flatten the authors' dictionaries to a list of all their values (e.g., 'id', 'name', 'org')
    author_list = []
    for author in authors:
        author_list.extend(list(author.values()))  # Add all values from the author dictionary to the list
    return author_list

data['authors'] = data['authors'].apply(convert_authors_to_list)


data.to_json('CleanDataSet.json', orient = 'records', indent=4)