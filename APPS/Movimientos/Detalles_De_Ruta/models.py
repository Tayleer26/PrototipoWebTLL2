from django.db import models

from APPS.Catalogos.Rutas.models import Rutas
from APPS.Catalogos.Vehiculo.models import Vehiculo
from APPS.Movimientos.Trabajadores.models import Trabajadores


# Create your models here.
class Detalles_De_Ruta(models.Model):
    Descripcion = models.TextField(max_length=300)
    Turno = models.CharField(max_length=20)
    Fecha = models.DateTimeField()
    idTrabajadores = models.ForeignKey(Trabajadores, on_delete=models.RESTRICT)
    idVehiculos = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT)
    idRutas = models.ForeignKey(Rutas, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Turno