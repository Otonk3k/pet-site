import imp
import re
from django.shortcuts import render, redirect
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'fast'
    feature1.details = 'our site is very quick'
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        if password == retype_password:          
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not the same')
            return redirect('register')
        
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def test(request):
    posts = [1, 2, 3, 'numer post', 'some random shit', 7, 'a;slkdjfg']
    return render(request, 'tests.html', {'posts': posts})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'not true')
            return redirect('login')
   
    else:
        return render (request, 'login.html')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})