from django.shortcuts import render
from mysite.models import Book
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Book.objects.all()
    now = datetime.now()
    return render (request, 'index.html', locals())

def showpost(request,slug):
    post = Book.objects.get(slug=slug)
    return render(request, 'post.html', locals())