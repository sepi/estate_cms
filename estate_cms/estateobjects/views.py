# from django.shortcuts import render
from django.views.generic import DetailView, ListView 
from .models import EstateObject

class EstateObjectDetailView(DetailView):
    model = EstateObject

