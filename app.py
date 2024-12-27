# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from documentRetrieval import search
import json
import time
previous_query=None
docs_to_load=None
total_results=None
app = Flask(__name__)
CORS(app)
@app.route('/search', methods=['GET'])
def search_endpoint():
    global previous_query, previous_query, total_results,docs_to_load
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    print(page)
    start=time.time()
    if query!=previous_query:
        docs_to_load = search(query)
        total_results=len(docs_to_load)
        previous_query=query
    print(total_results)
    docs = getDocs(docs_to_load,page)
    # ddocs = [json.loads(doc) for doc in docs]
    # for doc in ddocs:
    #     print(f'The title is {doc['title']}')
    #     print(f'The keywords is {doc['keywords']}')
    #     print(doc["abstract"])
    #     print("\n--------------------------------------")

    results = []
    for doc in docs:
        doc_data = json.loads(doc)
        results.append({
            'id': doc_data['id'],
            'title': doc_data['title'],
            'description': doc_data['abstract'],
            'authors': [authors['name'] for authors in doc_data["authors"]],
            'date': doc_data['year'],
            'citations': doc_data['n_citation'],
            'url': doc_data['url'][0]
        })
    
    results_per_page = 10
    total_pages = (total_results + results_per_page - 1) // results_per_page
    search_time=time.time()-start
    response = {
        'results': results,
        'total_pages': total_pages,
        'total_results': total_results,
        'search_time': search_time  # You can add actual search time if needed
    }
    
    return jsonify(response)

def getDocs(docs_to_load,page):
    stack = []
    docs = []
    i = 0
    start_index=(page-1)*10
    end_index=start_index+10
    with open("TheCleanData2.0.json", "r") as file:
        for document in docs_to_load[start_index:end_index]:
            doc = "{"
            stack.clear()
            file.seek(document[0])
            stack.append(file.read(1))
            while len(stack) != 0:
                doc += file.read(1)
                if doc[-1] == "{":
                    stack.append("{")
                elif doc[-1] == "}":
                    stack.pop()
            docs.append(doc)
            
    return docs

if __name__ == '__main__':
    print('Ali')
    app.run(debug=True, port=8000)