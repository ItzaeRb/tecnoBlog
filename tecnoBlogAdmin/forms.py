from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_posts(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=500)
    contenido = forms.CharField(max_length=2000)
    autor = forms.CharField(max_length=100)
    fecha = forms.DateField()
    imagen = forms.ImageField()
