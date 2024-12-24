# aplication1/forms.py
from django import forms

class TestForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    correo = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    edad = forms.IntegerField(label='Edad')
    