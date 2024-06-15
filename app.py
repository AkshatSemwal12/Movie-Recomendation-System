import streamlit as st
import pickle

st.title("Movie Recommendation System")

movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend_movies(movie):
    movie_index = movie_list[movie_list['title'] == movie].index
    if len(movie_index) > 0:
        movie_index = movie_index[0]
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
        recommendations = [movie_list.iloc[i[0]].title for i in movies_list]
        return recommendations
    else:
        return []

option = st.selectbox(
    'Choose a movie',
    movie_list['title'].values)

if st.button("Recommend", type="primary"):
    recommendations = recommend_movies(option)
    if recommendations:
        for movie in recommendations:
            st.write(movie)
    else:
        st.write('No recommendations found for this movie.')