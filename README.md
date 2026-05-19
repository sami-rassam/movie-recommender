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
- Add posters using TMDB API
- Deploy to Streamlit or Render
