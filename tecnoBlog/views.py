from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

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


def signout(request):
    logout(request)
    return redirect(inicio)
