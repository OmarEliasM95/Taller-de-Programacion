from django.contrib import admin
from .models import producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Precio', 'Existencias')

admin.site.register(producto, ProductoAdmin)
