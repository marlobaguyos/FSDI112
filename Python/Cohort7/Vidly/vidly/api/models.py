from django.db import models
from tastypie.resources import ModelResource
from rental.models import Movie, Genre


# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.object.all()
        resource_name = 'movies'