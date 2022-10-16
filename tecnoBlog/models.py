from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idUsuario = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=60)
    apellidoMaterno = models.CharField(max_length=60)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    tipoUsuario = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

class Blogs(models.Model):
    idBlog = models.IntegerField()
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=60)
    fecha = models.DateTimeField(auto_now_add=True)# le pone automaticamente la hora y la fecha.
    
    def __str__(self):
        return self.titulo + ' --> creado por --> ' + self.autor 


