import json

from django.http import JsonResponse
from django.views import View

from movies.models import *
# Create your views here.

class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        