from django.db import models
from django.db.models import Model

from APPS.Catalogos.Persona.models import Persona


# Create your models here.
class Trabajadores(models.Model):
    identificacion  = models.CharField(max_length=19)
    Codigo = models.CharField(max_length=3)
    Cargo = models.CharField(max_length=50)
    Salario = models.CharField(max_length=20)
    idPersona = models.ForeignKey (Persona, on_delete = models.RESTRICT)

    def __str__(self):
        return self.identificacion