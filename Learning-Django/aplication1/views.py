from django.shortcuts import render
from django.http import HttpResponse 
from .forms import TestForm

def holaDjango(request): 
    return HttpResponse("Hello, world. This is the index view of aplication1 on django project :D") 

def holaPersona(request):
    return HttpResponse("Hola como estas")

def formulario(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'formulario.html', {'mensaje': 'Formulario enviado con éxito'})
    else:
        form = TestForm()
    return render(request, 'formulario.html', {'form': form})

#otro request
def about(request):
    about_content = {'about': 'This is the about page, how are you?, more content is this page' }
    return render(request, "about.html", about_content)