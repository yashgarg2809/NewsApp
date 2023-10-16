from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('business/', views.business, name = 'business'),
    path('sports/', views.sports, name = 'sports'),
    path('technology/', views.technology, name = 'technology'),
    path('entertainment/', views.entertainment, name = 'etertainment'),
    path('health/', views.health, name = 'health'),
    path('science/', views.science, name = 'science'),
    path('newsletter/', views.newsletter, name = 'newsletter'),


]