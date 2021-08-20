from django.urls import path

from movies.views import MovieView, MovieDetailView, ReviewDetailView, ReviewView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', MovieDetailView.as_view()),
    path('movies/<int:movie_id>/review/', ReviewDetailView.as_view()),
    path('reviews/', ReviewView.as_view()),
]
