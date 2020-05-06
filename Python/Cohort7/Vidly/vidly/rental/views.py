from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
# MVC python manage.py runserver

# Defining an endpoint
def index(request):
    return HttpResponse("Hello World!")