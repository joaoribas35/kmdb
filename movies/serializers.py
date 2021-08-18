from rest_framework import serializers
from .models import Movie, Genre, Review


import ipdb


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

        depth = 1

    def create(self, validated_data):
        genres = validated_data.pop('genres')

        movie = Movie.objects.create(
            **validated_data)

        for genre in genres:
            item = Genre.objects.get_or_create(
                name=genre['name'])[0]
            movie.genres.add(item)

        return movie


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

        depth = 1
