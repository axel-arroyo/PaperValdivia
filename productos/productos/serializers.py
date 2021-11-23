from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')
        read_only_fields = ['slug']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = ('__all__')
        read_only_fields = ['slug']

class ItemSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(required=False)
    vendidos = serializers.IntegerField(required=False)
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('nombre', 'descripcion', 'precio', 'vendidos', 'imagen_url', 'categoria', 'subcategoria', 'slug')
        read_only_fields = ['slug']

    def get_imagen_url(self, obj):
        request = self.context.get('request')
        imagen_url = obj.imagen.url
        return request.build_absolute_uri(imagen_url)