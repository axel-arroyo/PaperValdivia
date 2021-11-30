from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("perfil", perfil),
    path("registro", registro),
    path("login", login),
    path("logout", logout),
]
