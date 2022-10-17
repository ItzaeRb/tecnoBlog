from django.shortcuts import render, redirect

#librerías para el login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import HttpResponse
from tecnoBlog.forms import UserRegisterForm, UserEditForm
from tecnoBlog.models import *


# Create your views here.
def inicio(request):
    return render(request, "homePage.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                return render(request, "verPerfil.html")
            else:
                #Si los datos de autenticacion no son correctos:
                return render(request, "login.html", {"form": form})
        return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})


def registroUsuario(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect("/login")
        else:
            return render(request, "login.html", {"form":form})
    form = UserRegisterForm()
    return render(request, "registroUsuario.html", {"form":form})



def verPosts(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPosts.html", {"blogs": blogs})

@login_required
def verPostsUser(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPostsUsuarios.html", {"blogs": blogs})


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
def perfilView(request):
    return render(request, 'verPerfil.html')