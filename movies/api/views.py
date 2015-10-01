from rest_framework.viewsets import ModelViewSet
from .. import models
from . import serializers


class PersonViewSet(ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class RoleViewSet(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer


class GenreViewSet(ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class SeriesViewSet(ModelViewSet):
    queryset = models.Series.objects.all()
    serializer_class = serializers.SeriesSerializer
