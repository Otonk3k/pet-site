from importlib.resources import path
from django import views
from django.shortcuts import render
from django.views import View

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
]