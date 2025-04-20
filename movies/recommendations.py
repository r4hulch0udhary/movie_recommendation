from django.db import connection


def collaborative_filtering(user_id):
    # Use SQL Query to get top 5 highest-rated movies
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title FROM movies_movie ORDER BY rating DESC LIMIT 5")
        top_movies = cursor.fetchall()
    return [movie[1] for movie in top_movies]


def content_based_filtering(user_id):
    # Use SQL Query to get the last rated movie and find similar movies
    with connection.cursor() as cursor:
        cursor.execute("SELECT movie_id FROM movies_rating WHERE user_id = %s ORDER BY id DESC LIMIT 1", [user_id])
        last_rated = cursor.fetchone()
        if last_rated:
            cursor.execute("SELECT title FROM movies_movie WHERE genre = (SELECT genre FROM movies_movie WHERE id = %s) AND id != %s LIMIT 5", [last_rated[0], last_rated[0]])
            similar_movies = cursor.fetchall()
            return [movie[0] for movie in similar_movies]
    return [] 