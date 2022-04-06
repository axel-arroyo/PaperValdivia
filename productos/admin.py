from django.contrib import admin
from .models import Caracteristica, Item, Categoria, Imagen, Subcategoria

class CategoriaAdminManager(admin.ModelAdmin):
    exclude = ('slug',)

class ItemAdminManager(admin.ModelAdmin):
    exclude = ('slug',)

class SubcategoriaManager(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Item, ItemAdminManager)
admin.site.register(Categoria, CategoriaAdminManager)
admin.site.register(Imagen)
admin.site.register(Subcategoria, SubcategoriaManager)
admin.site.register(Caracteristica)