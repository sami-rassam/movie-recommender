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

## Final Project Reflection

### What worked well

This project successfully demonstrates how a content-based movie recommendation system can be built from raw movie metadata and deployed through a simple Flask web application. The recommender uses descriptive movie features such as genres, keywords, overview, cast and director to create a combined `tags` column, which is then transformed into numerical vectors using text vectorisation. Cosine similarity is then used to identify films with similar content features.

One of the strongest parts of the project is that the recommendation logic is easy to understand and explain. Rather than acting as a black-box model, the system recommends films based on clear similarities in content. For example, if two films share similar genres, themes, cast members or directors, they are more likely to be recommended together. This makes the project suitable for demonstrating core machine learning concepts such as feature engineering, text preprocessing, vectorisation and similarity measurement.

The project also benefits from using TMDB rating information. By including fields such as `vote_average`, `vote_count`, `popularity` and a weighted TMDB rating, the recommender can go beyond simple similarity and consider the quality and reliability of each film’s rating. This helps reduce the risk of recommending films that may be similar but poorly rated or supported by very few votes.

Another successful part of the project is the end-to-end workflow. The project moves from exploratory data analysis and model development in Jupyter Notebook to deployment through a Flask web app. This shows the full data science project lifecycle, including data loading, cleaning, feature engineering, model building, testing, saving model files and creating a user-facing application.

### What limitations remain

Although the recommender works well as a content-based system, it has some important limitations. The model only recommends films based on movie metadata, so it does not learn from individual user behaviour, preferences or viewing history. This means every user receives the same recommendations for a selected movie, regardless of their personal taste.

Another limitation is that the model depends heavily on the quality of the available metadata. If a film has a short overview, missing keywords, incomplete cast information or poorly labelled genres, the recommendations may be less accurate. The system also treats the combined text features as a bag of words, meaning it does not fully understand deeper meaning, context or relationships between words.

The project also has limited evaluation. Content-based recommenders are harder to evaluate than standard classification or regression models because there is no single correct answer for what should be recommended. At this stage, the recommendations are mainly assessed manually by checking whether the suggested films appear reasonable and share similar content features.

There may also be some issues with duplicate or similar movie titles. Although a `movie_display` column using title and release year helps distinguish films, a more robust production system would use unique movie IDs throughout the app to avoid confusion between films with the same or similar names.

Finally, the current Flask app is intentionally simple. It provides recommendations through a basic web interface, but it does not yet include user accounts, saved preferences, movie posters, advanced search, filtering options or live API integration.

### How the model could be improved

The model could be improved by adding collaborative filtering. This would allow the system to recommend films based on user behaviour, such as ratings or viewing patterns, rather than only movie content. For example, using a dataset such as MovieLens, a user-item rating matrix could be created and similarity between users or items could be calculated. This would make the recommender more personalised.

A hybrid recommendation system would be another strong improvement. This could combine content-based similarity with collaborative filtering and weighted TMDB ratings. For example, the final recommendation score could combine content similarity, predicted user preference and rating quality. This would make the system more balanced and closer to the type of recommender systems used by real platforms.

The text processing could also be improved. Instead of using only CountVectorizer, the project could compare CountVectorizer with TF-IDF to see whether reducing the importance of very common words improves recommendation quality. More advanced natural language processing methods, such as word embeddings or transformer-based sentence embeddings, could also be used to capture deeper semantic meaning in movie overviews and descriptions.

The app could also be enhanced by adding movie posters, release year, genres, runtime and rating information to the recommendation results. This would make the user interface more informative and visually appealing. A search bar could replace the dropdown list to make the app easier to use, especially as the number of movies increases.

The project could also include a stronger evaluation section. Possible evaluation methods include checking genre overlap between the selected movie and recommendations, measuring average similarity scores, comparing recommendations from CountVectorizer and TF-IDF, and manually reviewing examples across different genres. This would make the analysis more rigorous and show a stronger understanding of model performance.

### How this project relates to real-world recommender systems

This project reflects the basic principles used by real-world recommender systems on platforms such as Netflix, Amazon, Spotify and YouTube. These platforms use recommendation algorithms to help users discover relevant content from very large catalogues. The core idea is similar: use data about items, users or interactions to rank and suggest content that is likely to be useful or interesting.

The content-based approach used in this project is especially relevant when user behaviour data is limited or unavailable. For example, a new platform may not yet have enough user ratings or viewing history to build a collaborative filtering model. In this situation, item metadata such as genre, description, cast, director and keywords can still be used to generate useful recommendations.

However, real-world recommender systems are usually more advanced than this project. They often combine multiple approaches, including content-based filtering, collaborative filtering, popularity trends, user demographics, contextual data and real-time interaction data. They may also consider business rules, diversity, freshness, user engagement and fairness when ranking recommendations.

This project is therefore a strong foundation for understanding recommender systems. It demonstrates the core workflow behind recommendation engines while leaving clear opportunities for future development. By extending it with collaborative filtering, hybrid scoring, stronger evaluation and a more polished user interface, the project could become a much more realistic example of how recommendation systems are designed and deployed in industry.
