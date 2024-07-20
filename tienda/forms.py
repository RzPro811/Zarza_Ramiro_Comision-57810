from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Registrar_Usuario(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =  ["username", "email", "password1", "password2"]

class Editar_Usuario(UserChangeForm):
    email      = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre",     max_length=50, required=True)
    last_name  = forms.CharField(label="Apellido",   max_length=50, required=True)
    password   = forms.CharField(label="Contraseña", max_length=50, required=True)
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password"]

class Crear_Avatar_Form(forms.Form):
    imagen = forms.ImageField(required=True)

class PeluchesForm(forms.Form):
    producto    = forms.CharField(max_length=50, required=True)
    precio      = forms.IntegerField(required=True)
    disponibles = forms.IntegerField(required=True)
    imagen      = forms.ImageField(required=False)
    
class CartasForm(forms.Form):
    juego            = forms.CharField(max_length=50, required=True)
    adultos          = forms.BooleanField(required=False)
    cantidad_cartas  = forms.IntegerField(required=True)
    precio           = forms.FloatField(required=True)
    disponibles      = forms.IntegerField(required=True)
    imagen           = forms.ImageField(required=False)

class FigurasAccionForm(forms.Form):
    figura      = forms.CharField(max_length=50, required=True)
    origen      = forms.CharField(max_length=50, required=True)
    fabricante  = forms.CharField(max_length=50, required=True)
    precio      = forms.FloatField(required=True)
    disponibles = forms.IntegerField(required=True)
    imagen      = forms.ImageField(required=False)

class JuegosMesaForm(forms.Form):
    juego       = forms.CharField(max_length=50, required=True)
    adultos     = forms.BooleanField(required=False)
    piezas      = forms.IntegerField(required=True)
    precio      = forms.FloatField(required=True)
    disponibles = forms.IntegerField(required=True)
    imagen      = forms.ImageField(required=False)