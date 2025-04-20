from celery import shared_task
from .models import Movie
import requests
from .recommendations import collaborative_filtering, content_based_filtering
from django.core.mail import send_mail
from django.db import connection

@shared_task
def update_recommendations():
    # Logic to update movie recommendations for all users
    print("Updating recommendations...")
    # Example: Iterate over all users and update their recommendations
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM auth_user")
        users = cursor.fetchall()
        for user_id in users:
            collaborative_filtering(user_id)
            content_based_filtering(user_id)

@shared_task
def process_new_rating(user_id, movie_id, score):
    # Logic to process a new rating and update recommendations
    print(f"Processing new rating for user {user_id} and movie {movie_id}...")
    # Update recommendations based on the new rating
    collaborative_filtering(user_id)
    content_based_filtering(user_id)


@shared_task
def import_movie_data(api_url):
    # Background task to import movie data from an external API
    print(f"Importing movie data from {api_url}...")
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = response.json()
        for movie in movies:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO movies_movie (title, genre, release_year) VALUES (%s, %s, %s)", [movie['title'], movie['genre'], movie['release_year']])
        print(f"Imported {len(movies)} movies.")
    else:
        print("Failed to import movie data.")