from ast import Pass
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from theFinalProject.view import homePage #codifica la contrase;a
from .models import *
from .forms import UserRegisterForm, blogForm, UserEditForm, changePasswordForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
def inicio(request):
    return render(request, "homePage.html")

def signup(request):
    if request.method == 'GET':
            return render(request, 'signup.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #de la clase User voy a utilizar de todos sus objetos un metodo llamado create_user espera el usuario y contrase;a que vienen de request.POST['username']
                #print(request.POST)
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save() # creamos el user, y lo guardamos en base de datos con el save()
                login(request, user) #autentica el usuario, login es un metodo viene de django.
                return redirect(signin) #lo envia a la funcion inicio
            except: #si no se puede crear usuario, renderiza el signup y muestra el error
                return render(request, 'signup.html', {'form':UserCreationForm, 'error':'No se pudo crear el usuario, intente nuevamente'})
        return render(request, 'signup.html', {'form':UserCreationForm, 'error':'Las pass no coinciden'})

def registro(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(signin)
        else:
            return render(request, 'registro.html', {'form': form})
    form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})



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
