from django.urls import path

from movies.views import MovieView, MovieDetailView, ReviewView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', MovieDetailView.as_view()),
    path('movies/<int:movie_id>/review/', ReviewView.as_view()),

]
