from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Movie, Review
from .serializers import MovieSerializer, MovieDetailSerializer, ReviewSerializer
from .permissions import MoviePermissions, ReviewPermissions

import ipdb


class MovieView(ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermissions]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermissions]

    def get_serializer_class(self):
        user = self.request.user

        if user.is_anonymous:
            return MovieSerializer

        return super().get_serializer_class()

    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    lookup_url_kwarg = "movie_id"


class ReviewView(ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermissions]

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    lookup_url_kwarg = "movie_id"
