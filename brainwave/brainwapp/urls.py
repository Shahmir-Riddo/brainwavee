from django.contrib import admin
from django.urls import path
from . import views
from brainwapp.models import Profile


urlpatterns = [
    path('', views.index, name="index"),
    path('blogwriter/', views.blogwriter, name="blogwriter"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('productdescwriter/', views.productdescwriter, name="productdescwriter"),
    path('appgenerator/', views.paragenerator, name="paragenerator"),
    path('emailgenerator/', views.emailgenerator, name="emailgenerator"),
    path('lyricsgenerator/', views.lyricsgenerator, name="lyricsgenerator"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('items/', views.items, name="items")
    
]
