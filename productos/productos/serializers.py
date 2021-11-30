from .models import *
from rest_framework import serializers

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = ('__all__')
        read_only_fields = ['slug']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True, source='subcategoria_set')
    class Meta:
        model = Categoria
        fields = ('slug', 'nombre', 'subcategories')
        read_only_fields = ['slug']
        depth = 1


class ItemSerializer(serializers.ModelSerializer):
    imagenes = serializers.SerializerMethodField('get_imagenes')
    class Meta:
        model = Item
        fields = ('nombre', 'descripcion', 'precio', 'stock','vendidos', 'categoria', 'subcategoria', 'slug', 'imagenes')
        read_only_fields = ['slug','vendidos']

    def get_imagenes(self, obj):
        request = self.context.get('request')
        # return [img.imagen.url for img in obj.imagenes.all()]
        return [request.build_absolute_uri(img.imagen.url) for img in obj.imagenes.all()]
