from django.shortcuts import render
from .models import Post, Category
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
def home_page(request):
    posts=Post.objects.filter(status='published')
    categories = Category.objects.all()
    return render(request,'news/home.html',{'posts':posts,'categories':categories})

def single_page(request,pk):
    #post=Post.objects.get(id = pk)
    post=get_object_or_404(Post,id=pk,status='published')
    #if post.status!='published':
        #return HttpResponseNotFound("<h1>Page not found</h1>")
    return render(request,'news/single_post.html',{'post':post})
    # else:
        #  raise Http404("post does not exist")
       
def category_list(request,pk):
    category=get_object_or_404(Category,pk=pk)
    posts = category.post_set.all()
    categories = Category.objects.all()
    return render(request,
                  'news/category_list.html',
                  {'posts':posts,
                   'category':category, 'categories':categories}

                  )
def author_post_list(request,pk):
    author=get_object_or_404(User,pk=pk)
    posts = author.post_set.all()
    categories = Category.objects.all()
    return render(request,'news/author_post_list.html',{'author':author,'posts':posts,'categories':categories} )
