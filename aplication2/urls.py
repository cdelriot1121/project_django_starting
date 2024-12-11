from django.urls import path
from aplication2 import views

urlpatterns = [
    path('home/', views.Respuesta, name='respuesta'),
]
