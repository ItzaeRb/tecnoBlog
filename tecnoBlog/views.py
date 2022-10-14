from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from tecnoBlog.forms import UserRegisterForm
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
            user = AuthenticationForm(username = user, password = pwd)
            if user is not None:
                login_request(request, user)
                return render(request, "homePage.html")
            else:
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
            return render(request, "registroUsuario.html", {"form":form})
    form = UserRegisterForm()
    return render(request, "registroUsuario.html", {"form":form})

def verPosts(request=None):
    blogs = Blogs.objects.all() #Trae todo
    return render(request, "verPosts.html", {"blogs": blogs})

def nuevoPost(request):
    if request.method == 'POST':
        blog = Blogs(idBlog = request.POST['idPost'], titulo = request.POST['tituloPost'], subtitulo = request.POST['subtituloPost'], contenido = request.POST['myeditor'], autor = request.POST['autorPost'], fecha = request.POST['fechaPost'])
        blog.save()
        blogs = Blogs.objects.all()    
        return render(request, "verPosts.html", {"blogs": blogs})
    return render(request, "nuevoPost.html")


#def login(request):
#    if request.method == 'GET':
#        return render(request, 'login.html', {'form': UserCreationForm})
#    else:
#        if request.POST['password1'] ==  request.POST['password2']:
#            try:        
#                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
#                user.save() # lo guarda dentro de la base de datos
#                return HttpResponse('Usuario creado')
#            except:
#                return HttpResponse('no  pudo crear el usuario')
#        return HttpResponse('Pass do not match')
