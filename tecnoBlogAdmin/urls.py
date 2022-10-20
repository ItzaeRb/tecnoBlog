from re import template
from django.urls import path
from tecnoBlogAdmin.views import *
from tecnoBlog.views import aboutUsAdmin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('homePageAdmin/', homePageAdmin),
    path('tecnoBlogAdmin/', inicioAdmin),
    path('AboutUsAdmin/', aboutUsAdmin),
    path('tecnoBlogAdmin/login', loginAdmin),
    path('logoutAdmin/', LogoutView.as_view(template_name = 'homePage.html')),
    path('tecnoBlogAdmin/nuevoPost', nuevoPost),
    path('tecnoBlogAdmin/verPostsAdmin',verPostsAdmin),
    path('tecnoBlogAdmin/readPosts', readPosts),
    path('tecnoBlogAdmin/postComplete/<id_blog>', postComplete),
    path('tecnoBlogAdmin/update_posts/<id_blog>', update_posts),
    path('tecnoBlogAdmin/delete_posts/<id_blog>', delete_posts),

]