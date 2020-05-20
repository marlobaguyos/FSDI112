from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
# MVC python manage.py runserver

# Defining an endpoint
def index(request):
    all_movies = Movie.objects.all() # read Movie table to a list
    return render(request, 'index.html', { 'title': 'Moview Catalog', 'movies': all_movies })

def catalog(request):
    return render(request, 'catalog.html')

# about send your name

def about(request):
    return HttpResponse("Marlo")


# Working on it

def soon(request):
    return render(request, 'comingSoon.html')