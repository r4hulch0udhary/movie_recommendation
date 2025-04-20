from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie, Rating, Watchlist
from movies.serializers import MovieSerializer, RatingSerializer, WatchlistSerializer
from movies.recommendations import collaborative_filtering, content_based_filtering
from django.db import connection


class MovieListCreateView(APIView):
    """View to list all movies or create a new movie using stored procedures."""
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.callproc('get_movies')
            movies = cursor.fetchall()
        return Response(movies)

    def post(self, request):
        title = request.data.get('title')
        genre = request.data.get('genre')
        release_year = request.data.get('release_year')
        with connection.cursor() as cursor:
            cursor.callproc('insert_movie', [title, genre, release_year])
        return Response({'status': 'Movie added'}, status=201)


class MovieDetailView(APIView):
    """View to retrieve, update, or delete a movie using stored procedures."""
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.callproc('get_movie_by_id', [pk])
            movie = cursor.fetchone()
        return Response(movie)

    def put(self, request, pk):
        title = request.data.get('title')
        genre = request.data.get('genre')
        release_year = request.data.get('release_year')
        with connection.cursor() as cursor:
            cursor.callproc('update_movie', [pk, title, genre, release_year])
        return Response({'status': 'Movie updated'})

    def delete(self, request, pk):
        with connection.cursor() as cursor:
            cursor.callproc('delete_movie', [pk])
        return Response({'status': 'Movie deleted'})


class RatingListCreateView(APIView):
    """View to list all ratings or create a new rating using stored procedures."""
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.callproc('get_ratings')
            ratings = cursor.fetchall()
        return Response(ratings)

    def post(self, request):
        user_id = request.data.get('user_id')
        movie_id = request.data.get('movie_id')
        score = request.data.get('score')
        with connection.cursor() as cursor:
            cursor.callproc('insert_rating', [user_id, movie_id, score])
        return Response({'status': 'Rating added'}, status=201)


class WatchlistListCreateView(APIView):
    """View to list all watchlist entries or create a new entry using stored procedures."""
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.callproc('get_watchlist')
            watchlist = cursor.fetchall()
        return Response(watchlist)

    def post(self, request):
        user_id = request.data.get('user_id')
        movie_id = request.data.get('movie_id')
        watched = request.data.get('watched', False)
        with connection.cursor() as cursor:
            cursor.callproc('insert_watchlist', [user_id, movie_id, watched])
        return Response({'status': 'Watchlist entry added'}, status=201)


class RecommendationView(APIView):
    """View to get movie recommendations based on user preferences."""
    def get(self, request, *args, **kwargs):
        user = request.user
        collaborative_recommendations = collaborative_filtering(user)
        content_recommendations = content_based_filtering(user)
        return Response({
            'collaborative': collaborative_recommendations,
            'content_based': content_recommendations
        })
