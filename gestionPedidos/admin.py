from django.contrib import admin

# Register your models here.

from gestionPedidos.models import clientes, articulos, pedidos

admin.site.register(clientes)
admin.site.register(articulos)
admin.site.register(pedidos)
