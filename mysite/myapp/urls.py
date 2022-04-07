from importlib.resources import path
from django import views
from django.shortcuts import render
from django.views import View

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name="post"),
    path('tests', views.test, name='test')
]