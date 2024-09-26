from django.contrib import admin

from APPS.Catalogos.Vehiculo.models import Vehiculo


# Register your models here.
@admin.register(Vehiculo)

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['Placa', 'NumVehicle', 'Descripcion', 'capacidad']
    search_fields = ['Placa']
