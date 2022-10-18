from django.db import models

# Create your models here.

class Blogs(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=60)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="imagenes", null=True, blank = True)

    
    def __str__(self):
        return f"Título:{self.titulo} - Subtítulo:{self.subtitulo} - Contenido: {self.contenido} - Autor: {self.autor} - Fecha: {self.fecha} - Imagen: {self.imagen}"


class Mensajes(models.Model):
    destinatario = models.CharField(max_length=30)
    contenido = models.CharField(max_length=150)
    remitente = models.CharField(max_length=30)
    fecha = models.DateField()
    