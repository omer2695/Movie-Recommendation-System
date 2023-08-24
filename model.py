# The machine learning model code.

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

"""Using CountVectorizer to Extracting Features from Text

CountVectorizer is a great tool provided by the scikit-learn library in Python. 
It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text."""

"""What is NLTK used for? The Natural Language Toolkit (NLTK) is a platform used for building Python programs that work with human
language data for applying in statistical natural language processing (NLP). 
It contains text processing libraries for tokenization, 
parsing, classification, stemming, tagging and semantic reasoning."""


def ML_model(movie):
    data_frame = pd.read_csv("new_movies.csv")
    cv = CountVectorizer(max_features=5000, stop_words='english')
    cv.fit_transform(data_frame['tags']).toarray().shape
    vectors = cv.fit_transform(data_frame['tags']).toarray()
    
    data_frame['tags'] = data_frame['tags'].apply(stem)

    similarity = cosine_similarity(vectors)
    movie_list_recommend = recommend(movie, data_frame, similarity)
    return movie_list_recommend


def stem(text):
    ps = PorterStemmer()
    y = []
    for i in text.split():
        y.append(ps.stem(i))

    return "".join(y)


def recommend(movie, data_frame, similarity):
    movie_list_recommend = []
    movie_index = data_frame[data_frame['title'] == movie].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        movie_list_recommend.append(data_frame.iloc[i[0]].title)
        
    return movie_list_recommend
