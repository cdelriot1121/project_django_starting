from django.contrib.auth.hashers import make_password
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Asegúrate de que la contraseña sea hasheada antes de guardar
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


#nuevo modelo customer para aplicar ORM

class Customer(models.Model):
    nombre_reservante = models.CharField(max_length=255)
    dia_reserva = models.CharField(max_length=10)
    asientos = models.IntegerField()
    menu = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_reservante} - {self.dia_reserva}"
