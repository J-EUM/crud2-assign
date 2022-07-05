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
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name' : actor.last_name,
                }
            )

        return JsonResponse({'results': results}, status=200)

