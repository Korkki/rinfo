from rest_framework import serializers
from .. import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('first_name', 'last_name', 'birthday', 'bio', 'photo')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ('person', 'movie', 'name', 'photo')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    cast = PersonSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = ('title', 'description', 'slug', 'published', 'runtime', 'cast', 'director', 'score', 'series',
                  'poster', 'genres', 'created', 'modified')


class SeriesSerializer(serializers.ModelSerializer):
    episodes = MovieSerializer(many=True)

    class Meta:
        model = models.Series
        fields = ('title', 'description', 'slug', 'created', 'modified', 'parent', 'episodes')
