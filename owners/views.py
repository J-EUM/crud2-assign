#from curses import ACS_GEQUAL
#import email
import json

#from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from owners.models import *
# Create your views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name=data['name'], 
            email=data['email'], 
            age=data['age']
            )
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = Dog.objects.filter(owner_id=owner.id)
            dogs_list = []
            for dog in dogs:
                dogs_list.append(
                    {
                        'dog_name': dog.name,
                        'dog_age': dog.age
                    }
                    
                )
            results.append(
                {
                    'name': owner.name,
                    'email': owner.email,
                    'age': owner.age,
                    'dog_list': dogs_list
                }
            )
        return JsonResponse({'results': results}, status=200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data['name'], 
            age=data['age'], 
            owner=Owner.objects.get(name=data['owner'])
            )
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    'name': dog.name,
                    'age': dog.age,
                    'owner_name': dog.owner.name
                }
            )
        return JsonResponse({'results': results}, status=200)
