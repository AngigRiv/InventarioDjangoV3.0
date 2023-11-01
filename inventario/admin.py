from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Personal)
admin.site.register(GrupoProveedor)
admin.site.register(LineaArticulo)
admin.site.register(SublineaArticulo)
admin.site.register(UnidadMedida)
admin.site.register(Marca)
admin.site.register(Articulo)
admin.site.register(Inventario)
admin.site.register(ItemInventario)
#admin.site.register(Usuario)