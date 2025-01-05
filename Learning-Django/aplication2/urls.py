# aplication2/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('bebidas/<str:bebida>', views.bebidaItems), # bebida = cafe o cerveza
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
