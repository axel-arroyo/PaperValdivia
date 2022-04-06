from django.urls import path

from .views import *

urlpatterns = [
    path("panel", productsPanel),
    path("nuevoProducto", nuevoProducto),
    path("nuevaCategoria", nuevaCategoria),
    path("edit/<slug:slug>", editarProducto),
    # path("nuevaCategoria", registro),
]
