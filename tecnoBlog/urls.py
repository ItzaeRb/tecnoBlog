from re import template
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('signup/', signup),
    path('signin/', signin),
    path('logout/', signout),
    path('homePage/', inicio),
    path('verPosts/', verPosts),
    path('nuevoPost/', nuevoPost),
    path('editarUsuario/', editarUsuario),
    path('registro/', registro),
    path('changePass/', changePass),
    path('perfil/', perfilView),
    path('agregarAvatar/', agregarAvatar)
]
