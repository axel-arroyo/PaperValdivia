from django import forms
from django.forms import widgets
from .models import Categoria, Item

class AgregarItem(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}), required=False)
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Precio'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Stock'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagen'})

class AgregarCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre'})

