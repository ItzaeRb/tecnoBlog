from re import template
from django.urls import path
from tecnoBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('login/', login_request),
    path('signIn/', registroUsuario),
    path('tecnoBlog/nuevoPost', nuevoPost),
    path('tecnoBlog/verPosts', verPosts),
]