from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movies = pickle.load(open('model.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def generate_explanation(selected_movie_index, recommended_movie_index):
    selected_tags_raw = movies.iloc[selected_movie_index].tags
    recommended_tags_raw = movies.iloc[recommended_movie_index].tags

    if isinstance(selected_tags_raw, list):
        selected_tags = set(selected_tags_raw)
    else:
        selected_tags = set(str(selected_tags_raw).split())

    if isinstance(recommended_tags_raw, list):
        recommended_tags = set(recommended_tags_raw)
    else:
        recommended_tags = set(str(recommended_tags_raw).split())

    shared_tags = selected_tags.intersection(recommended_tags)

    if len(shared_tags) == 0:
        return "Recommended because it has a similar overall content profile."

    shared_tags_sample = list(shared_tags)[:5]

    return "Recommended because it shares similar features such as: " + ", ".join(shared_tags_sample)

def recommend(movie):
    movie_index = movies[movies['movie_display'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:21]
    
    recommendations = []
    
    for i in movie_list:
        recommendations.append({
    'title': movies.iloc[i[0]].movie_display,
    'rating': round(movies.iloc[i[0]].weighted_tmdb_rating, 2),
    'category': movies.iloc[i[0]].rating_category,
    'poster_url': movies.iloc[i[0]].poster_url,
    'explanation': generate_explanation(movie_index, i[0])
})
    
    recommendations_df = pd.DataFrame(recommendations)
    
    recommendations_df = recommendations_df.sort_values(
        by='rating',
        ascending=False
    )
    
    return recommendations_df.head(8).to_dict(orient='records')

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