from django.urls import path
from aplication2 import views

urlpatterns = [
    path('bebidas/<str:bebida>', views.bebidaItems) #bebida = cafe o cerveza
]
