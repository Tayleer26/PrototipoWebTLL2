from django.contrib import admin

from APPS.Movimientos.Contrato.models import Contratos
from APPS.Movimientos.Detalles_De_Ruta.models import Detalles_De_Ruta


# Register your models here.
@admin.register(Detalles_De_Ruta)
# Register your models here.
class Detalle_De_RutaAdmin(admin.ModelAdmin):
    list_display = ['Descripcion','Turno','Fecha','idTrabajadores','idVehiculos','idRutas']
    search_fields = ['Turno']