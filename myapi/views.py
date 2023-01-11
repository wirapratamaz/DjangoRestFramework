from django.shortcuts import render
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import viewsets

# Create your views here.
# class that provides a default set of CRUD using ModelViewSet
class HeroViewSet(viewsets.ModelViewSet):
    #property will select all the records of Hero table order by 'name'
    queryset = Hero.objects.all().order_by('name')
    #property will use the HeroSerializer class to convert the model into JSON
    serializer_class = HeroSerializer