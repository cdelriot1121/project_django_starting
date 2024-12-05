from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def holaDjango(request): 
    return HttpResponse("Hello, world. This is the index view of aplication1 on django project :D") 

def holaPersona(request):
    return HttpResponse("Hola como estas")
