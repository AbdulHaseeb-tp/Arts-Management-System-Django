from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . views import signup, login

urlpatterns = [
    path('signup/', signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # default django auth urls for login,logout, etc.....
    path('', include('django.contrib.auth.urls')),
]