import streamlit as st
import pickle
import pandas as pd
import os
import gdown
import requests
#similarity.pkl download
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=18Mtt68SKl7UDFIV-kz_UwQrzfVD5pCQ8"
    gdown.download(url, "similarity.pkl", quiet=False)
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=b18404e6a4d424ddf83d06ef9e369821&language=en-US'.format(movie_id)
    )
    data = response.json()

    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"
def recommend(movie):

    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    recommend_movies=[]
    recommend_movies_poster=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id'] 
        #fetch poster from api
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_poster


movies = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies)
movies_list = movies['title'].values



similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox("Select  a movie from here", movies_list)
if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.write(names[i])
            st.image(poster[i])



