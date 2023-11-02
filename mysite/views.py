from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render (request, 'index.html', locals())

def showpost(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', locals())