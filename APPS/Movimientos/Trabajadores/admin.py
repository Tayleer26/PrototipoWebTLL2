from django.contrib import admin
from APPS.Movimientos.Trabajadores.models import Trabajadores

@admin.register(Trabajadores)
class TrabajadoresAdmin(admin.ModelAdmin):
    list_display = ['identificacion', 'Codigo', 'Cargo', 'Salario', 'idPersona']
    search_fields = ['identificacion']