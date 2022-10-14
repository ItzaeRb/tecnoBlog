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

    def __str__(self):
        return f"ID:{self.idUsuario} - Nombre:{self.nombre} - Apellido paterno:{self.apellidoPaterno} - Apellido materno: {self.apellidoMaterno} - Username: {self.username} - Password: {self.password} - Tipo de usuario: {self.tipoUsuario} - Descripción: {self.descripcion}"

class Blogs(models.Model):
    idBlog = models.IntegerField()
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=60)
    fecha = models.DateField()

    def __str__(self):
        return f"ID:{self.idBlog} - Título:{self.titulo} - Subtítulo:{self.subtitulo} - Contenido: {self.contenido} - Autor: {self.autor} - Fecha: {self.fecha}"

