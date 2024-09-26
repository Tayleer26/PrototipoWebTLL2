from django.db import models

from APPS.Movimientos.Contrato.models import Contratos


# Create your models here.
class Pagos(models.Model):
    Codigo = models.CharField(max_length=3)
    Monto = models.CharField(max_length=20)
    Fecha = models.DateTimeField()
    idContratos = models.ForeignKey(Contratos, null=True, on_delete=models.SET_NULL)
    # Referencia al mismo modelo usando 'self'

    def __str__(self):
        return self.Codigo