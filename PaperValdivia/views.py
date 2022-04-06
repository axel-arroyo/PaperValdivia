from django.shortcuts import render


# General
def index(request):
    context = {"usuario": request.user}
    return render(request, 'index.html', context)

def descripcion(request):
    return render(request, 'descripcion.html')

def descargables(request):
    return render(request, 'descargables.html')

# Catalogo
def catalogo(request):
    return render(request, 'catalogo/catalogo.html')

def categoriaView(request, categoria=None):
    context = {"categoria": categoria}
    return render(request, 'catalogo/catalogo.html', context)

def productView(request, cat_slug=None, prod_slug=None):
    if prod_slug is None:
        return render(request, 'catalogo/catalogo.html')
    context = {"producto": prod_slug, "categoria": cat_slug}
    return render(request, 'catalogo/producto.html', context)





