from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    Placa = models.CharField(max_length=7)
    NumVehicle= models.CharField(max_length=5)
    Descripcion = models.TextField()
    capacidad = models.CharField(max_length=20)

    def __str__(self):
        return self.Placa