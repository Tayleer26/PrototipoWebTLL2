from django.contrib import admin

from APPS.Catalogos.Persona.models import Persona


@admin.register(Persona)
# Register your models here.



# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['Nombres','Apellidos','Direccion','Telefono']
    search_fields = ['Nombres']