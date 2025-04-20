from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the movie.")
    genre = models.CharField(max_length=100, help_text="The genre of the movie.")
    release_year = models.IntegerField(help_text="The year the movie was released.")


class Rating(models.Model):
    SCORE_CHOICES = [
        (1, "1 - Poor"),
        (2, "2 - Fair"),
        (3, "3 - Good"),
        (4, "4 - Very Good"),
        (5, "5 - Excellent"),
    ]

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, help_text="The user who rated the movie.")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, help_text="The movie that was rated.")
    score = models.IntegerField(choices=SCORE_CHOICES, help_text="The rating score given by the user.")


class Watchlist(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,help_text="The user who added the movie to their watchlist.",)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, help_text="The movie added to the watchlist.")
    watched = models.BooleanField(default=False, help_text="Indicates whether the movie has been watched." )
