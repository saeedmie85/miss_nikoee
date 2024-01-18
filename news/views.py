from django.shortcuts import render
from .models import Post

def home_page(request):
    posts=Post.objects.all()
    return render(request,'news/tech-index.html',{'posts':posts})

def single_page(request,pk):
    post=Post.objects.get(id = pk)
    return render(request,'news/single_post.html',{'p':post})
