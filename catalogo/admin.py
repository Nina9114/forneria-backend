from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Productos, Categorias, Usuarios, Nutricional, Direccion, Roles

# Registrar los modelos para que se muestren en el admin
admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(Usuarios)
admin.site.register(Nutricional)
admin.site.register(Direccion)
admin.site.register(Roles)
