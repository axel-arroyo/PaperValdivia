from django.shortcuts import render
import requests

ipUsers = "http://localhost:8001/"

# General
def index(request):
    context = {"usuario": request.user}
    return render(request, 'index.html', context)

def descripcion(request):
    return render(request, 'descripcion.html')

# Catalogo
def catalogo(request):
    return render(request, 'catalogo/catalogo.html')

def categoriaView(request, cat=None):
    context = {"usuario": request.user}

def productView(request, cat_slug=None, prod_slug=None):
    if prod_slug is None:
        return render(request, 'catalogo/catalogo.html')
    context = {"producto": prod_slug, "categoria": cat_slug}
    return render(request, 'catalogo/producto.html', context)

# Usuarios
def registro(request):
    context = {"usuario": request.user}
    return render(request, 'usuarios/registro.html', context)

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['correo']
        password = request.POST['clave']
        response = requests.post(ipUsers+"login", data={'username': username, 'password': password})
        if response.status_code == 200:
            context['usuario'] = response.json()
            resp = render(request, 'usuarios/perfil.html', context)
            resp.set_cookie('token', response.json()['token'])
            return render(request, 'index.html', context)

    return render(request, 'usuarios/login.html', context)

def logout(request):
    context = {"usuario": request.user}
    return render(request, 'index.html', context)

def perfil(request):
    context = {"usuario": request.user}
    return render(request, 'usuarios/perfil.html', context)





