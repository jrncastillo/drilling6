from django.db import models
from django.conf import settings

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=20)
    precio = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20,default='Particular')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modoficacion = models.DateTimeField(auto_now=True)

    
