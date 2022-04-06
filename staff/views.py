from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# AdminView
@staff_member_required(login_url='/')
def productsPanel(request):
    return render(request, 'panel.html')

@staff_member_required(login_url='/')
def nuevoProducto(request):
    return render(request, 'nuevoProducto.html')

@staff_member_required(login_url='/')
def nuevaCategoria(request):
    return render(request, 'nuevaCategoria.html')

@staff_member_required(login_url='/')
def editarProducto(request, slug):
    context = {'slug': slug}
    return render(request, 'editarProducto.html', context)
