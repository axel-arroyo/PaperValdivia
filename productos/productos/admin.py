from django.contrib import admin
from .models import Item, Categoria

class CategoriaAdminManager(admin.ModelAdmin):
    exclude = ('slug',)

class ItemAdminManager(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Item, ItemAdminManager)
admin.site.register(Categoria, CategoriaAdminManager)