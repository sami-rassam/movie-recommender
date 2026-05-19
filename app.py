from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movies = pickle.load(open('model.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['movie_display'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]
    
    recommendations = []
    
    for i in movie_list:
        recommendations.append({
            'title': movies.iloc[i[0]].movie_display,
            'rating': round(movies.iloc[i[0]].weighted_tmdb_rating, 2),
            'category': movies.iloc[i[0]].rating_category,
            'poster_url': movies.iloc[i[0]].poster_url
        })
    
    recommendations_df = pd.DataFrame(recommendations)
    
    recommendations_df = recommendations_df.sort_values(
        by='rating',
        ascending=False
    )
    
    return recommendations_df.head(5).to_dict(orient='records')

@app.route('/')
def home():
    movie_list = movies['movie_display'].values
    return render_template('index.html', movie_list=movie_list)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    selected_movie = request.form['movie']
    recommendations = recommend(selected_movie)
    return render_template(
        'index.html',
        movie_list=movies['movie_display'].values,
        selected_movie=selected_movie,
        recommendations=recommendations
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)