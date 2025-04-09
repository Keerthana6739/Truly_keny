from django.urls import path,include
from .views import *
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def digital(request):
    return render(request, 'digital.html')
def music(request):
    return render(request, 'music.html')
def satellite(request):
    return render(request, 'satellite.html')
def movies(request):
    return render(request, 'movies.html')
def gaming(request):
    return render(request, 'gaming.html')
def elearning(request):
    return render(request, 'elearning.html')
def lottery(request):
    return render(request, 'lottery.html')
def ecommerce(request):
    return render(request, 'ecommerce.html')
def tours(request):
    return render(request, 'tours.html')
def about(request):
    return render(request, 'about.html')