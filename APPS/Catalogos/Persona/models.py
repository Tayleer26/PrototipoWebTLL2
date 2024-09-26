from django.db import models

# Create your models here.
class Persona(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.TextField()
    Telefono = models.CharField(max_length=8)


    def __str__(self):
        return self.Nombres