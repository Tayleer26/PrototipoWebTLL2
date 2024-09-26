# APPS/Movimientos/Contrato/models.py
from django.db import models
from APPS.Catalogos.Rutas.models import Rutas
from APPS.Movimientos.Estudiante.models import Estudiante  # Esta es la importación correcta

# Define tu modelo Contratos
class Contratos(models.Model):
    Codigo = models.CharField(max_length=3)
    FechaInicio = models.DateTimeField()
    FechaFIn = models.DateTimeField()
    Monto = models.CharField(max_length=20)
    Grado = models.CharField(max_length=10)
    idEstudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)  # Relaciona con el modelo Estudiante
    idRutas = models.ForeignKey(Rutas, on_delete=models.RESTRICT)  # Relaciona con el modelo Rutas

    def __str__(self):
        return self.Codigo