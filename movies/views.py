from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


from .models import Movie, Review
from .serializers import MovieSerializer, MovieDetailSerializer, ReviewSerializer, CreateReviewSerializer
from .permissions import MoviePermissions, ReviewDetailPermissions

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


class ReviewDetailView(CreateAPIView, UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewDetailPermissions]

    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer

    lookup_url_kwarg = "movie_id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        validated_data = serializer.is_valid(raise_exception=True)

        user = request.user
        movie_id = kwargs['movie_id']

        movie = get_object_or_404(Movie, id=movie_id)

        if movie.reviews.filter(critic_id=user.id).exists():
            return Response({"detail": "You already made this review."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        review = Review.objects.create(
            **validated_data, critic=user, movie=movie)

        response_serializer = CreateReviewSerializer(review)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):

        user = request.user
        movie_id = kwargs['movie_id']
        movie = get_object_or_404(Movie, id=movie_id)
        review = movie.reviews.get(critic_id=user.id)

        partial = kwargs.pop('partial', False)
        instance = review

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ReviewView(ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        critic = True if user.is_superuser == False else False

        if critic:
            queryset = Review.objects.filter(critic_id=user.id)
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
