from ast import Pass
from django.forms import PasswordInput
from django.shortcuts import render, redirect

#librerías para el login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import HttpResponse
from tecnoBlog.forms import UserRegisterForm, UserEditForm
from tecnoBlogAdmin.models import Blogs, Mensajes
from tecnoBlog.models import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from theFinalProject.view import homePage #codifica la contrase;a
from .forms import UserRegisterForm, blogForm, UserEditForm, changePasswordForm, avatarForm

# Create your views here.
def inicio(request):
    return render(request, "homePage.html")

def aboutUs(request):
    return render(request, "About.html")

@login_required
def inicioUsuario(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'homePageUsuario.html', {'avatar': avatar})
    

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'homePageUsuario.html', {'avatar': avatar})
            else:
                #Si los datos de autenticacion no son correctos:
                return render(request, "login.html", {"form": form})
        return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})


def registroUsuario(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request, "login.html", {"form":form})
    form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})


def verPostsUser(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPostsUsuarios.html", {"blogs": blogs})

def verPosts(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPosts.html", {"blogs": blogs})

def postCompleto(request, id_blog):
    blog = Blogs.objects.get(id = id_blog)
    return render(request,"postCompleto.html", {"blogs": blog})

def postCompletoUsr(request, id_blog):
    blog = Blogs.objects.get(id = id_blog)
    return render(request,"postCompletoUsr.html", {"blogs": blog})

@login_required
def editProfile(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario) 
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name  = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'homePage.html')
        else:
            return render(request, 'homePage.html', {'form':form})
    else: 
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        
    return render(request, 'editProfile.html', {'form':form, 'usuario':usuario}) 



@login_required
def signout(request):
    logout(request)
    return redirect(inicio)



@login_required
def nuevoPost(request):
    if request.method == 'POST':
        blog = Blogs(idBlog = request.POST['idPost'], titulo = request.POST['tituloPost'], subtitulo = request.POST['subtituloPost'], contenido = request.POST['myeditor'], autor = request.POST['autorPost'], fecha = request.POST['fechaPost'])
        blog.save()
        blogs = Blogs.objects.all()    
        return render(request, "verPosts.html", {"blogs": blogs})
    return render(request, "nuevoPost.html")


@login_required
def editarUsuario(request, usuario_id):
    user_basic_info = User.objects.get(id = usuario_id)
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            #datos a actualizar
            user_basic_info.username = form.cleaned_data.get("username")
            user_basic_info.email = form.cleaned_data.get("email")
            user_basic_info.first_name = form.cleaned_data.get("first_name")
            user_basic_info.last_name = form.cleaned_data.get("last_name")
            user_basic_info.save()
            usuario = User.objects.all()
            return render(request, "homePage.html", {'usuario':usuario})
        else:
            return render(request, "homePage.html", {"form": form})
    else:
        form = UserEditForm(initial={"email": usuario.email, "username": usuario.username, "first_name":usuario.first_name, "last_name": usuario.last_name})
    return render(request, "editarUsuario.html", {"form":form, "usuario":usuario})


@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = usuario)
        #form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'homePage.html')
    else:
        form = PasswordChangeForm(request.user)
        #form = ChangePasswordForm(user = request.user)
    return render(request, 'changePassword.html', {'form': form, 'usuario': usuario})


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = avatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'homePageUsuario.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = avatarForm()
        except:
            form = avatarForm()
    return render(request, 'agregarAvatar.html', {'form': form})

@login_required
def perfilView(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'verPerfil.html', {'avatar': avatar})



@login_required
def nuevoMensaje(request):
    if request.method == 'POST':
        mensaje = Mensajes(destinatario = request.POST['destinatario'], contenido = request.POST['contenido'], remitente = request.POST['remitente'], fecha = request.POST['fecha'])
        mensaje.save()
        mensajes = Mensajes.objects.all()    
        return render(request, "verMensajes.html", {"mensajes": mensajes})
    return render(request, "nuevoMensaje.html")

def verMensajes(request=None):
    mensajes = Mensajes.objects.all() #Trae todo
    return render(request, "verMensajes.html", {"mensajes": mensajes})
