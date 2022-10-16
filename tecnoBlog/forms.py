from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget= forms.TextInput(attrs={"placeholder": "email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "first_name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "last_name"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "password"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        help_text = {k:"" for k in fields}

class blogForm(ModelForm):
    class meta:
        model = Blogs # el formulkario esta basado en los atributos del modelo Blogs
        fields = ['titulo', 'subtitulo', 'contenido']
