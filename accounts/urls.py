from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [


    path('login/',views.sign_in,name='SignIn'),
    path('signup/',views.sign_up,name='SignUp'),
    path('logout/',views.user_logout, name='logOut'),



]
