from django.shortcuts import render
from tecnoBlog.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def nuevoPost(request):
    if request.method == 'POST':
        blog = Blogs(idBlog = request.POST['idPost'], titulo = request.POST['tituloPost'], subtitulo = request.POST['subtituloPost'], contenido = request.POST['myeditor'], autor = request.POST['autorPost'], fecha = request.POST['fechaPost'])
        blog.save()
        blogs = Blogs.objects.all()    
        return render(request, "verPosts.html", {"blogs": blogs})
    return render(request, "nuevoPost.html")