# from django.shortcuts import render

# # Create your views here.

# ------------------------

# from django.shortcuts import render
# from django.http import HttpResponse

# def main(request):
#     return HttpResponse("Hello World")

# ------------------------

from django.shortcuts import render
from rest_framework import generics, status
from .models import Room 
from .serializers import RoomSerializer

def main(request):
    return HttpResponse("Hello World")

