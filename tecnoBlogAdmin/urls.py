from re import template
from django.urls import path
from tecnoBlogAdmin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('tecnoBlogAdmin/', inicioAdmin),
    path('tecnoBlogAdmin/login', loginAdmin),
    path('logoutAdmin/', LogoutView.as_view(template_name = 'homePage.html')),
    path('tecnoBlogAdmin/nuevoPost', nuevoPost),
    path('tecnoBlogAdmin/verPostsAdmin',verPostsAdmin),
]