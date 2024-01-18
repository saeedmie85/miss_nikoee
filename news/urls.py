
from .views import home_page, single_page
from django.contrib import admin
from django.urls import path, include
app_name='news'
urlpatterns = [
    path('',home_page),
    path('post/<int:pk>',single_page,name='single_page')
]
