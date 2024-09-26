from django.contrib import admin

from APPS.Movimientos.Contrato.models import Contratos


# Register your models here.
@admin.register(Contratos)
# Register your models here.
class ContratosAdmin(admin.ModelAdmin):
    list_display = ['Codigo','FechaInicio','FechaFIn','Monto','Grado','idEstudiante','idRutas']
    search_fields = ['Codigo']