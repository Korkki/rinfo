from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'movie')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'runtime', 'score', 'series')
    list_filter = ('genres',)
    search_fields = ('title',)
