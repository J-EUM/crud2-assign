import json

from django.http import JsonResponse
from django.views import View

from movies.models import *
# Create your views here.
class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            movies_list = []
            movies = Movie.objects.filter(actor__id=actor.id)
            for movie in movies:
                movies_list.append(
                    {
                        'movie_title': movie.title
                    }
                )
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name' : actor.last_name,
                    'movies_list' : movies_list
                }
                
            )

        return JsonResponse({'results': results}, status=200)

