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
from tecnoBlogAdmin.models import *
from tecnoBlog.models import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from theFinalProject.view import homePage #codifica la contrase;a
from .forms import UserRegisterForm, blogForm, UserEditForm, changePasswordForm, avatarForm

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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(signin)
        else:
            return render(request, "login.html", {"form":form})
    form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})



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
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form':AuthenticationForm})
    else:
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is None: #si la autenticacion no fue valida.
            return render(request, 'signin.html', {'form':AuthenticationForm, 'error': 'No se pudo validar el usuario'})
        else:
            login(request, user)#loguea al usuario ya atutenicado y guarda la sesion
            return redirect('/homePage/')

@login_required
def signout(request):
    logout(request)
    return redirect(inicio)

@login_required
def verPosts(request=None):
    forms = Blogs.objects.all() #Trae todo
    return render(request, "verPosts.html", {"forms": forms})

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
def changePass(request):
    usuario = request.user #traemos los datos del usuario
    if request.method == 'POST':
        form = changePasswordForm(data = request.POST, user = usuario) #un form que nos da django
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'homePage.html')
    else:
        form = changePasswordForm(user = request.user)
    return render(request, 'changePass.html', {'form':form}, {'usuario': usuario})

@login_required
def perfilView(request):
    return render(request, 'perfil.html')


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = avatarForm(request.POST, request.FILE) # .file para tener la interpretacion de un archivo.
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            return render(request, 'home.html', {'avatar': avatar[0]}.image.url) # oapra mostrar el avatar todas lsa veces que se llame a home.html
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = avatarForm()
        except:
            form = avatarForm()
    return render(request, 'agregarAvatar.html', {'form': form}) 
