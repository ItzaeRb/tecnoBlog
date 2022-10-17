from re import template
from django.urls import path
from tecnoBlogAdmin.views import *
from tecnoBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('tecnoBlogAdmin/nuevoPost', nuevoPost),
]