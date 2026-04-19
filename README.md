__CONTENT BASED MOVIE RECOMENDATION SYSTEM__

A smart and interactive Movie Recommendation System built using Machine Learning that suggests movies based on user preferences. This project demonstrates how content-based filtering can be used to recommend similar movies using metadata such as genres, keywords, cast, and crew.


__PROJECT OVERVIEW__

In today’s world, users often struggle to find movies that match their interests due to the vast amount of available content. This project solves that problem by recommending movies that are similar to the one selected by the user.
The system uses a content-based filtering approach, where movies are recommended based on their similarity in features rather than user ratings.


__HOW IT WORKS__

✅The dataset contains movie information such as title, genres, keywords, cast, and crew.

✅Important features are combined into a single text (tags).

✅Text data is converted into vectors using techniques like Count Vectorization.

✅Cosine similarity is used to calculate similarity between movies.

✅When a user selects a movie, the system finds and displays the most similar movies.


__FEATURES__

•Programming Language: Python

•Libraries: Pandas, NumPy, Scikit-learn

•Frontend/UI: Streamlit

•Machine Learning: Content-Based Filtering


__PROJECT STRUCTURE__

movie-recommendation-system

 │── app.py
 
 │── movies.pkl 
 
 │── similarity.pkl 
 
 │── requirements.txt
 
 │── README.md


__PROJECT SETUP__

for run this project locally

✅git clone https://github.com/aayushgi/movie-recommender

✅cd movie-recommender-system 

✅pip install -r requirements.txt 

✅streamlit run app.py


__FUTURE IMPROVMENT__

Improve search functionality

Enhance UI

Add ratings and reviews

__PROJECT LINK__

https://movie-recommender-ayushgi.streamlit.app/


--AYUSH SAXENA
This is all about the project 
