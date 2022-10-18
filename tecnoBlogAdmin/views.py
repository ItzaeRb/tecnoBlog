import re
from tkinter.messagebox import NO
from django.shortcuts import render, redirect

#librerías para el login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import HttpResponse
from tecnoBlog.forms import UserRegisterForm, UserEditForm
from tecnoBlog.models import *
from tecnoBlogAdmin.models import *
from tecnoBlogAdmin.forms import *

@login_required
def homePageAdmin(request):
    return render(request, "homePageAdmin.html")

# Create your views here.
@login_required
def inicioAdmin(request):
    return render(request, "homePageAdmin.html")

def loginAdmin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                return render(request, "homePageAdmin.html")
            else:
                #Si los datos de autenticacion no son correctos:
                return render(request, "loginAdmin.html", {"form": form})
                
        return render(request, "loginAdmin.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "loginAdmin.html", {"form":form})


@login_required
def nuevoPost(request):
    if request.method == 'POST':
        blog = Blogs()
        blog.titulo = request.POST.get('tituloPost')
        blog.subtitulo = request.POST.get('subtituloPost')
        blog.contenido = request.POST.get('myeditor')
        blog.autor = request.POST.get('autorPost')
        blog.fecha = request.POST.get('fechaPost')
        blog.imagen = request.FILES.get('imagenPost')
        blog.save()
        blogs = Blogs.objects.all()    
        return render(request, "verPosts.html", {"blogs": blogs})
    return render(request, "nuevoPost.html")


@login_required
def verPostsAdmin(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPostsAdmin.html", {"blogs": blogs})

@login_required
def readPosts(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "read_posts.html", {"blogs": blogs})


def update_posts(request, id_blog):
    blog = Blogs.objects.get(id = id_blog)
    if request.method == 'POST':
        formulario = form_posts(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog.titulo = informacion['titulo']
            blog.subtitulo = informacion['subtitulo']
            blog.contenido = informacion['contenido']
            blog.autor = informacion['autor']
            blog.fecha = informacion['fecha']
            blog.imagen = informacion['imagen']
            blog.save() 
            posts = Blogs.objects.all()
            return render (request, "read_posts.html", {"blogs":posts})
    else:
        formulario = form_posts(initial={'titulo':blog.titulo, 'subtitulo':blog.subtitulo, 'contenido':blog.contenido, 'autor':blog.autor, 'fecha':blog.fecha, 'imagen':blog.imagen})
    return render(request, "editarPost.html", {"formulario":formulario})


def delete_posts(request, id_blog):
    blog = Blogs.objects.get(id = id_blog)
    blog.delete()
    posts = Blogs.objects.all()    
    return render(request, "read_posts.html", {"blogs": posts})





