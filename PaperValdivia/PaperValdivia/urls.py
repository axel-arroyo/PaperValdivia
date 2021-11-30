from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Admin
    path('staff/', include('staff.urls')),
    # General
    path('', index, name="index"),
    path('descripcion', descripcion, name="descripcion"),
    path('descargables', descargables, name="descargables"),
    # Catalogo
    path('catalogo/', catalogo),
    path('catalogo/<slug:categoria>', categoriaView),
    path('catalogo/<slug:cat_slug>/<slug:prod_slug>', productView),
    # Usuarios
    path('usuarios/', include('usuarios.urls')),
]
