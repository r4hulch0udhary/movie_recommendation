from django.urls import path
from movies.auth import RegisterUserAPIView, LogoutAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from movies.views import (
    MovieListCreateView,
    MovieDetailView,
    RatingListCreateView,
    WatchlistListCreateView,
    RecommendationView
)

urlpatterns = [
    # Auth Urls
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    
    # Movie Urls
    path("movies/", MovieListCreateView.as_view(), name="movie-list-create"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("ratings/", RatingListCreateView.as_view(), name="rating-list-create"),
    path("watchlists/", WatchlistListCreateView.as_view(), name="watchlist-list-create"),
    path('recommendations/', RecommendationView.as_view(), name='recommendations'),
]
