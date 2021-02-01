from django.contrib import admin

# Register your models here.

from gestionPedidos.models import clientes, articulos, pedidos


class clienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
    search_fields=("nombre","telefono")

class articuloAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    list_filter=("seccion",)

class pedidoAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(clientes, clienteAdmin)
admin.site.register(articulos, articuloAdmin)
admin.site.register(pedidos, pedidoAdmin)
