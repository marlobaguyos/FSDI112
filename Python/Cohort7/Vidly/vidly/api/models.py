from django.db import models
from tastypie.resources import ModelResource, ALL
from rental.models import Movie, Genre
from tastypie.authorization import Authorization


# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ['title', 'release_year', 'price']
        filtering = {
            'release_year': ALL, 
            'price': ALL,
            'title': ALL
        }
        allowed_method = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization()

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_method = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization()


"""

Ordering:
/movies/?order_by=price
/movies/?order_by=-price

Filtering:
/movies/?price__lt=10
/movies/?price__gt=10
/movies/?price=10
/movies/?release_year__gt=2018
/movies/?title__contains=forest

"""