from re import template
from django.urls import path
from tecnoBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('login/', login_request),
    path('signIn/', registroUsuario),
    path('logout/', LogoutView.as_view(template_name = 'homePage.html'), name="Logout" ),
    path('tecnoBlog/verPosts', verPosts),
    path('tecnoBlog/verPostsUsr',verPostsUser),
    path('profile/editarPerfil', editProfile),
    path('profile/cambiarPassword', changepass),
    path('profile/', perfilView),
]