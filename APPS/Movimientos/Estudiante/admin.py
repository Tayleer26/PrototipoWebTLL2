from django.contrib import admin

from APPS.Movimientos.Estudiante.models import Estudiante


# Register your models here.
@admin.register(Estudiante)
# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['Codigo','Edad','idPersona']
    search_fields = ['Codigo']