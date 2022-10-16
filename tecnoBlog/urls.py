from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('signup/', signup),
    path('signin/', signin),
    path('logout/', signout),
    path('homePage/', inicio),
]