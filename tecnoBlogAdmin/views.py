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
# Create your views here.
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
        blog = Blogs(idBlog = request.POST['idPost'], titulo = request.POST['tituloPost'], subtitulo = request.POST['subtituloPost'], contenido = request.POST['myeditor'], autor = request.POST['autorPost'], fecha = request.POST['fechaPost'])
        blog.save()
        blogs = Blogs.objects.all()    
        return render(request, "verPosts.html", {"blogs": blogs})
    return render(request, "nuevoPost.html")