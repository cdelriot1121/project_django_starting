from django.urls import path 
from . import views 


#este urls aplication es opcional para crear el view y parametrizar el urls propia de la aplication
urlpatterns = [ 
    path('', views.index, name=''), 
] 