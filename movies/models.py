from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()


class Genre(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, related_name="genres")


class Review(models.Model):
    critic = models.ForeignKey(
        User, on_delete=CASCADE)
    start = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    movie = models.ForeignKey(
        Movie, on_delete=CASCADE, related_name="reviews")
