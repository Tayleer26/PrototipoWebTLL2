from django.contrib import admin

from APPS.Movimientos.Pagos.models import Pagos


# Register your models here.
@admin.register(Pagos )
# Register your models here.
class PagosAdmin(admin.ModelAdmin):
    list_display = ['Codigo','Monto','Fecha','idContratos']
    search_fields = ['Codigo']

