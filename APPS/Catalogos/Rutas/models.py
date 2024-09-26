from django.db import models

# Create your models here.
class Rutas(models.Model):
    Sector = models.CharField(max_length=50)
    Zona = models.CharField(max_length=50)

    def __str__(self):
        return self.Sector