from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('login/', login_request),
    path('nuevoPost/', nuevoPost)
]