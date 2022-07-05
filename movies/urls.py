from django.urls import path, include

from movies.views import *

urlpatterns = [
    path('/actors', ActorsView.as_view()),
]
