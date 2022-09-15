from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('login/', LoginView, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name=-'register')
]