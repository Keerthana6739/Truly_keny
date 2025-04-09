from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('digital/', views.digital, name='digital'),
    path('music', views.music, name='music'),
    path('satellite', views.satellite, name='satellite'),
    path('movies', views.movies, name='movies'),
    path('gaming', views.gaming, name='gaming'),
    path('elearning', views.elearning, name='elearning'),
    path('lottery', views.lottery, name='lottery'),
    path('ecommerce', views.ecommerce, name='ecommerce'),
    path('tours', views.tours, name='tours'),
    path('about', views.about, name='about'),


]
