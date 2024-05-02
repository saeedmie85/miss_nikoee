
from .views import home_page, single_page, category_list,author_post_list
from django.contrib import admin
from django.urls import path, include

app_name='news'
urlpatterns = [
    path('',home_page,name='home'),
    path('post/<int:pk>',single_page,name='single_page'),
    path('cat/<int:pk>',category_list, name='post_category'),
    path('author/<int:pk>',author_post_list,name='author_posts')
]  
