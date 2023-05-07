from django.contrib import admin
from django.urls import path
from .views.view import Song
urlpatterns = [
   path("songs/", Song,name='songs'),
]
