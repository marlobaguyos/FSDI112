from django.contrib import admin
from .models import Movie, Genre

# Create template Models
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "genre")
    list_display_links = ("id", "title")
    #exclude = ("price", )
    #fields = ("release_year", "title", "genre", "image", "price", "in_stock")

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)