from asyncio.windows_events import NULL
import imp
from django.shortcuts import redirect, render
from .models import Post, Comment
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
def post(request, pk):
    comments = Comment.objects.all()
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts, 'comments': comments})
def makepost(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        post = Post.objects.create(
            title = title, body = body
        )
    return render(request, 'makepost.html')
