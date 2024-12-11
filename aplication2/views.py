from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Respuesta(request):
    path = request.path
    response = HttpResponse("Esta es una respuesta HttpResponse")
    return response