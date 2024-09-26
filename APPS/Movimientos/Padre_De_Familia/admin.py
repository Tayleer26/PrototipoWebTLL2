# admin.py
from django.contrib import admin
from APPS.Movimientos.Padre_De_Familia.models import Padre_De_Familia

@admin.register(Padre_De_Familia)
class Padre_De_FamiliaAdmin(admin.ModelAdmin):
    list_display = ['identificacion']
    search_fields = ['identificacion']