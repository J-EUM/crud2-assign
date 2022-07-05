from django.urls import path, include

from movies.views import *

urlpatterns = [
    path('', MoviesView.as_view()),
    path('/actors', ActorsView.as_view()),
]
