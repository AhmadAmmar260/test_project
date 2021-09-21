from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('type_of_account',index,name='index'),
   path('login',login,name='login'),
   path('register',register,name='register'),
   path('test',adding),
   path('home',home,name='home')
]
