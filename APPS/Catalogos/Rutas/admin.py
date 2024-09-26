from django.contrib import admin

from APPS.Catalogos.Rutas.models import Rutas


# Register your models here.
@admin.register(Rutas)
# Register your models here.



# Register your models here.
class RutasAdmin(admin.ModelAdmin):
    list_display = ['Sector','Zona']
    search_fields = ['Sector']