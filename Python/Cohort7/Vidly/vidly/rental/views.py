from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
# MVC python manage.py runserver

# Defining an endpoint
def index(request):
    return HttpResponse("Hello World!")

# about send your name

def about(request):
    return HttpResponse("Marlo")


# Working on it

def soon(request):
    return HttpResponse("Not done! Go away!")