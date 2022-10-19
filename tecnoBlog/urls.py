from re import template
from django.urls import path
from tecnoBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('tecnoBlog/homePage', inicioUsuario),
    path('login/', login_request),
    path('signIn/', registroUsuario),
    path('logout/', LogoutView.as_view(template_name = 'homePage.html'), name="Logout" ),
    path('tecnoBlog/verPosts', verPosts),
    path('tecnoBlog/verPostsUser',verPostsUser),
    path('tecnoBlog/postCompleto/<id_blog>', postCompleto),
    path('tecnoBlog/postCompletoUsr/<id_blog>', postCompletoUsr),
    path('profile/editarPerfil', editProfile),
    path('profile/cambiarPassword', changepass),
    path('profile/agregarAvatar/', agregarAvatar),
    path('perfil/', perfilView),
    path('profile/nuevoMensaje', nuevoMensaje),
    path('profile/verMensajes', verMensajes),
]
