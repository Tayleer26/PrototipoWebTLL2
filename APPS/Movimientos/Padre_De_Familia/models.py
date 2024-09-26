# models.py
from django.db import models
from APPS.Catalogos.Persona.models import Persona

# Create your models here.
class Padre_De_Familia(models.Model):
    identificacion  = models.CharField(max_length=14)
    idPersona = models.ForeignKey(Persona, on_delete=models.RESTRICT)

    def __str__(self):
        return self.identificacion