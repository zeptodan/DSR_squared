<p align="center">
  <img src="https://raw.githubusercontent.com/zeptodan/DSR_squared/main/Assets/Banner.png" width="100%" height = auto>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]() [![React](https://img.shields.io/badge/React-18.2.0-blue.svg)]() [![Python](https://img.shields.io/badge/Python-3.9+-green.svg)]() [![Flask](https://img.shields.io/badge/Flask-3.1+-black.svg)]() [![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)]
# DSR²

A modern, fast scientific and academic paper search engine enhanced with ML.

## Features

- **Lightning Fast**: Sub-second search results with optimized indexing
- **Intelligent Ranking**: Modern relevance scoring algorithms (TF-IDF)
- **Synonym search**: Fast query expansion with synonyms, powered by machine learning 
- **Modern UI**: Clean, responsive interface built with React
- **Mobile Ready**: Fully responsive design for all devices




<p align="center">
  <img src="https://raw.githubusercontent.com/zeptodan/DSR_squared/main/Assets/Project_Demo_Vid.webp" width="100%" height = auto>
</p>

## Tech Stack


<p align="center"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" alt="React" width="40" height="40"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="TypeScript" width="40" height="40"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tailwindcss/tailwindcss-original.svg" alt="Tailwind CSS" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="Flask" width="40" height="40"/>
 <img src="https://cdn-lfs.hf.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/942cad1ccda905ac5a659dfd2d78b344fccfb84a8a3ac3721e08f488205638a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D%22hf-logo.svg%22%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1750096735&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA5NjczNX19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzk0MmNhZDFjY2RhOTA1YWM1YTY1OWRmZDJkNzhiMzQ0ZmNjZmI4NGE4YTNhYzM3MjFlMDhmNDg4MjA1NjM4YTA%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=MA7YFwwBAjU8KGNGIHwQmFfptFf03AIm%7EawmagRtJj2jlg%7Est7bbMKAu-FbGmTElmssPNwg7kXaStogER%7EYxh%7E1mmW0TpdEUhwdX9WiHlWo6NXjmtsrUpx1QLvYi7M-zYK67UkPRVK0lfXcvuKoGbjteQ3Qc1YtpmYTv52jOIkeKgEbYELjS8nvJ1OMFUYGAmIJCMgw2uyLJClX8Twd0g-5L87i-HbfNdFtJvzfuwkfov7iH87EPaq0AfF2GXRgdvrnK4MVr3OVjVDXVlY0hKNYF%7EQUXBzYY1D4GUvZ-xSHXURC5RdOrhrh5KnQ6A0B8utqPcuEssaenC4tO7AwDdg__&Key-Pair-Id=K3RPWS32NSSJCE" alt = "Sentence Transformers" height="50"/>
 </p> 
<p align="center"> 

<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Meta_Platforms_Inc._logo_%28cropped%29.svg" alt="FAISS" width="auto" height="35"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg" alt="SpaCY" width="auto" height="40"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/JSON_vector_logo.svg" alt = "iJSON" height = "40" width = "auto"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" alt="Scikit Learn" width="auto" height="40"/>
</p>

## Performance

- **Search Speed**: < 1s average response time
- **Corpus**: 1 million+ scientific and academic papers

## 📋 Project Structure

```
DSR²/
├── Assets/
├── backend/
├── Barreling/
│   ├── BarrelingInverted.py
│   ├── Barrels.ipynb
│   └── actualBarrels.py
├── Cleaning/
│   └── DataCleaning.py
├── Indexing/
│   ├── Forward_Index.py
│   ├── Inverted_Index.py
│   └── lexicon.py
├── Searching/
│   ├── app.py
│   ├── documentAddition.py
│   ├── documentRetrieval.py
│   ├── ranking.py
│   ├── utils.py
│   └── requirements.txt
└── frontend/
    ├── app/
    ├── components/
    ├── lib/
    ├── public/
    └── styles/
```

## Data

The datasets and indices can all be downloaded [here](https://drive.google.com/drive/folders/1yDvounEtpnOgNOEnsvgFJX2m38jALtGl?usp=sharing)

## License

This project is licensed under the MIT License - see the [LICENSE](https://claude.ai/chat/LICENSE) file for details.

## Acknowledgments

- [Kaggle](https://www.kaggle.com/) for the large scientific paper dataset
- [Flask](https://fastapi.tiangolo.com/) for the excellent Python framework
- [React](https://reactjs.org/) for the amazing frontend library
- [v0.dev](https://v0.dev/) for allowing us to build such an amazing frontend



---

 <p align="center"> Made with ❤️ by 
  <a href="https://github.com/dmunish">Danish Munib</a>, 
  <a href="https://github.com/GHAURIEE">Nouman Ghauri</a>, 
  <a href="https://github.com/zeptodan">Muhammad Anas</a>
</p>
