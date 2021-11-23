from .models import Categoria, Item, Subcategoria
from .serializers import ItemSerializer, CategorySerializer, SubcategorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class ItemView(APIView):
    serializer_class = ItemSerializer
    def get(self, request):
        if request.method == 'GET':
            if request.GET.get('categoria'):
                items = Item.objects.filter(categoria=request.GET.get('categoria'))
                serializer = ItemSerializer(items, many=True, context={'request': request})
                return Response(serializer.data)
            elif request.GET.get('producto'):
                item = Item.objects.get(slug=request.GET.get('producto'))
                serializer = ItemSerializer(item, context={'request': request})
                return Response(serializer.data)
            else:
                items = Item.objects.all()
                serializer = ItemSerializer(items, many=True, context={'request': request})
                return Response(serializer.data)
    
    def post(self, request):
        if request.method == 'POST':
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)


class CategoryView(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Categoria.objects.all()
    
    def get(self, request):
        if request.method == 'GET':
            serializer = CategorySerializer(self.get_queryset(), many=True) 
            return Response(serializer.data)
    
    def post(self, request):
        if request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

class SubcategoryView(APIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        return Subcategoria.objects.all()
    
    def get(self, request):
        if request.method == 'GET':
            serializer = SubcategorySerializer(self.get_queryset(), many=True) 
            return Response(serializer.data)
    
    def post(self, request):
        if request.method == 'POST':
            serializer = SubcategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)