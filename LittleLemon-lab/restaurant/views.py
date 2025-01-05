# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.utils.text import slugify

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
#view menu
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu" : menu_data
    }
    return render(request, 'menu.html', main_data)
    
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
        nombre_ret = slugify(menu_item.nombre)
    else:
        menu_item = ''
        nombre_ret = '' 
    context = {
        'menu_item': menu_item,
        'nombre_ret': nombre_ret
    }
    return render(request, 'menu_item.html', context)