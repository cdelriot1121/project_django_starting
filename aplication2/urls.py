from django.urls import path
from aplication2 import views

urlpatterns = [
    path('bebidas/<str:bebida>', views.bebidaItems), #bebida = cafe o cerveza
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
