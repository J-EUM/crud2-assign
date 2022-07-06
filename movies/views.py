import json

from django.http import JsonResponse
from django.views import View

from movies.models import *
# Create your views here.
class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors_list = []
            actors = movie.actor_set.all()
            for actor in actors:
                actors_list.append(
                    {
                        'first_name': actor.first_name,
                        'last_name': actor.last_name
                    }
                )
            results.append(
                {
                    'title': movie.title,
                    'running_time': movie.running_time,
                    'actors_list': actors_list

                }
            )
        return JsonResponse({'results': results},)

    

class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name' : actor.last_name,
                    'movies_list' : [movie.title for movie in actor.movies.all()]
                }
                
            )

        return JsonResponse({'results': results}, status=200)
