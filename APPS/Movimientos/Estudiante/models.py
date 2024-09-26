from django.db import models

from APPS.Catalogos.Persona.models import Persona


# Create your models here.
class Estudiante(models.Model):
    Codigo = models.CharField(max_length=3)
    Edad = models.CharField(max_length=20)
    idPersona = models.ForeignKey(Persona, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Codigo