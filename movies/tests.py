from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .tasks import update_recommendations, process_new_rating, send_email_notifications, import_movie_data
from .recommendations import collaborative_filtering, content_based_filtering
from django.db import connection
from datetime import datetime

# Create your tests here.

class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie_data = {'title': 'Inception', 'genre': 'Sci-Fi', 'release_year': 2010}

    def test_create_movie(self):
        response = self.client.post(reverse('movie-list-create'), self.movie_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_movies(self):
        response = self.client.get(reverse('movie-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskTestCase(TestCase):
    def test_update_recommendations(self):
        result = update_recommendations.apply()
        self.assertIsNone(result.result)

    def test_process_new_rating(self):
        result = process_new_rating.apply(args=[1, 1, 5])
        self.assertIsNone(result.result)

    def test_send_email_notifications(self):
        result = send_email_notifications.apply(args=[1])
        self.assertIsNone(result.result)

    def test_import_movie_data(self):
        result = import_movie_data.apply(args=['http://example.com/api/movies'])
        self.assertIsNone(result.result)

class RecommendationTestCase(TestCase):
    def setUp(self):
        # Create a test user using raw SQL
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO auth_user (username, password, first_name, last_name, email, is_active, is_superuser, is_staff, date_joined) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, ['testuser', 'testpass', 'Test', 'User', 'testuser@example.com', True, False, False, datetime.now()])
            self.user_id = cursor.fetchone()[0]

    def tearDown(self):
        # Delete the test user using raw SQL
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM auth_user WHERE id = %s", [self.user_id])

    def test_collaborative_filtering(self):
        # Pass the user_id instead of a user object
        recommendations = collaborative_filtering(user_id=self.user_id)
        self.assertIsInstance(recommendations, list)

    def test_content_based_filtering(self):
        # Pass the user_id instead of a user object
        recommendations = content_based_filtering(user_id=self.user_id)
        self.assertIsInstance(recommendations, list)
