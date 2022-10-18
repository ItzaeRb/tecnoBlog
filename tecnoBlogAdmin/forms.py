from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_posts(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=60)
    contenido = forms.CharField(max_length=500)
    autor = forms.CharField(max_length=60)
    fecha = forms.DateField()
    imagen = forms.ImageField()
