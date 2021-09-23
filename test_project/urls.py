from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('type_of_account',index,name='index'),
   path('login1',login1,name='login1'),
   path('Registration',Registeration,name='Registration'),
   path('register',register,name='register'),
   path('test',adding),
   path('home',home,name='home'),
   path('ajax/username_validate/',validate_username,name="validate_username"),
   path('login',login3,name='login'),
   path('test',adding),
   path('get_data',get_data,name="name"),
   path('testing_data',testing_data)

]
