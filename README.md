# Movie Recommendation System

## Project Overview
This project builds a content-based movie recommendation system using TMDB movie data, Python, Flask and machine learning.

## Dataset
The project uses the TMDB 5000 Movies and Credits datasets.

## Methodology
- Data cleaning
- Feature extraction
- Text preprocessing
- CountVectorizer
- Cosine similarity
- Weighted TMDB rating
- Flask web app deployment

## How to Run
pip install -r requirements.txt
python app.py

## Docker
docker build -t movie-recommender .
docker run -p 5000:5000 movie-recommender

## Future Improvements
- Add collaborative filtering
- Add user accounts
- Deploy to Streamlit or Render


## Final Reflection

This project successfully built an end-to-end content-based movie recommendation system using TMDB movie metadata, Python, machine learning and Flask. The model uses features such as genres, keywords, overview, cast and director to create a combined text representation of each film. 

A key strength of the project is that the recommendation logic is explainable. The system recommends films because they share similar descriptive features, making it easier to understand than a black-box model. The project also demonstrates a complete workflow, from data cleaning and exploratory analysis through to model building, saving files and deploying the recommender in a Flask web app.

The main limitation is that the system is not personalised to individual users. It does not use viewing history, user ratings or behavioural data, so every user receives the same recommendations for a selected film. The quality of the recommendations also depends on the quality of the metadata. Missing or incomplete overviews, genres, keywords or cast details can reduce recommendation accuracy.

The model could be improved by adding collaborative filtering using a user-rating dataset such as MovieLens. A hybrid system could then combine content similarity, user-based recommendations and weighted TMDB ratings. The app could also be improved with search functionality & filters.
