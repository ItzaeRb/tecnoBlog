from django.db import models

# Create your models here.

class Blogs(models.Model):
    idBlog = models.IntegerField()
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=60)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="imagenes", null=True)

    def __str__(self):
        return f"ID:{self.idBlog} - Título:{self.titulo} - Subtítulo:{self.subtitulo} - Contenido: {self.contenido} - Autor: {self.autor} - Fecha: {self.fecha} - Imagen: {self.imagen}"

