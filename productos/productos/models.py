from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

def set_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nombre)

class Categoria(models.Model):
    slug = models.SlugField(max_length=128, unique=True, primary_key=True)
    nombre = models.CharField(max_length=128)
    def __str__(self) -> str:
        return self.slug

pre_save.connect(set_slug, sender=Categoria)

class Subcategoria(models.Model):
    slug = models.SlugField(max_length=128, unique=True, primary_key=True)
    nombre = models.CharField(max_length=128)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.slug

pre_save.connect(set_slug, sender=Subcategoria)

class Item(models.Model):
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    stock = models.IntegerField(default=1,verbose_name="Stock")
    precio = models.IntegerField(verbose_name="Precio")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, verbose_name="Subcategoría", null=True, blank=True)
    descripcion = models.CharField(default='',max_length=512, verbose_name="Descripcion")
    imagen = models.ImageField(upload_to='productos')
    vendidos = models.IntegerField(default=0, verbose_name="Vendidos")

    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self) -> str:
        return self.slug

pre_save.connect(set_slug, sender=Item)
# Create your models here.
