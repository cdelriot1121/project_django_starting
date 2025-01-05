# aplication2/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Usuario.objects.create(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def bebidaItems(request, bebida):
    items = {
        'cafe': 'cafe es una bebida del mundo para mantenerte activo y es muy rico',
        'cerveza': 'La cerveza es una bebida para disfrutar con amigos y familia',
    }

    descripcion = items[bebida]

    return HttpResponse(f"<h2> {bebida} </h2>" + descripcion)

