from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Respuesta(request):
    path = request.path
    return HttpResponse(path, content_type='text/html', charset='utf-8')