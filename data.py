import pandas as pd
import numpy as np
import ast


def file_preparation():

    movies_df = pd.read_csv("movies.csv")
    credits_df = pd.read_csv("credits.csv")
    movies_df = merge_file(movies_df, credits_df)

    movies_df['genres'] = movies_df['genres'].apply(convert)
    movies_df['keywords'] = movies_df['keywords'].apply(convert)
    # The funcation convets an object and the return list of the first 3 names.
    movies_df['cast'] = movies_df['cast'].apply(convert3)

    movies_df['crew'] = movies_df['crew'].apply(fetch_director)
    # split the overview to list of key words.
    movies_df['overview'] = movies_df['overview'].apply(lambda x: x.split())

    movies_df['genres'] = movies_df['genres'].apply(
        lambda x: [i.replace(" ", "") for i in x])
    movies_df['keywords'] = movies_df['keywords'].apply(
        lambda x: [i.replace(" ", "") for i in x])
    movies_df['cast'] = movies_df['cast'].apply(
        lambda x: [i.replace(" ", "") for i in x])
    movies_df['crew'] = movies_df['crew'].apply(
        lambda x: [i.replace(" ", "") for i in x])
    # Create col with all the tags
    movies_df['tags'] = movies_df['overview'] + movies_df['genres'] + \
        movies_df['keywords']+movies_df['cast']+movies_df['crew']

    new_movies_df = movies_df[['movie_id', 'title',
                               'popularity', 'vote_average', 'tags']]

    new_movies_df['tags'] = new_movies_df['tags'].apply(lambda x: ' '.join(x))

    new_movies_df['tags'] = new_movies_df['tags'].apply(lambda x: x.lower())

    save_file(new_movies_df, "new_movies.csv")


# The function merge 2 files onto 1
def merge_file(movies_df, credits_df):
    movies_df = movies_df.merge(credits_df, on='title')

    movies_df = movies_df[['movie_id', 'title', 'overview', 'genres',
                           'keywords', 'popularity', 'vote_average', 'cast', 'crew']]

    movies_df.dropna(inplace=True)

    return movies_df


# The function convert object to list
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L
# The function return the the name of the producer/director from all the crew members.


def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


def save_file(data_frame, file_name):
    try:
        data_frame.to_csv(file_name, index=False)
        print(f"Data saved to {file_name} successfully.")
    except Exception as e:
        print(f"Error saving data to {file_name}: {str(e)}")
