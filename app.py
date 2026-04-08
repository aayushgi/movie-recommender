import streamlit as st
import pickle
import pandas as pd
import os
import gdown
#similarity.pkl download
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=18Mtt68SKl7UDFIV-kz_UwQrzfVD5pCQ8"
    gdown.download(url, "similarity.pkl", quiet=False)
def recommend(movie):

    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies)
movies_list = movies['title'].values



similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox("Select  a movie from here", movies_list)
if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
#this is all through 