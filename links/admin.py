from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'category')
    list_filter = ('category', 'tags')
    search_fields = ('description',)
