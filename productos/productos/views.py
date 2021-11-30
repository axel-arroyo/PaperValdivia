from django.db.models import query
from .models import Categoria, Item, Subcategoria, Imagen
from .serializers import ItemSerializer, CategorySerializer, SubcategorySerializer

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response


class ResponsePagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page'
    max_page_size = 12


class ItemView(APIView):
    serializer_class = ItemSerializer
    paginator = ResponsePagination()
    def get(self, request):
        if request.method == 'GET':
            if request.GET.get('categoria'):
                paginator = ResponsePagination()
                items = Item.objects.filter(categoria=request.GET.get('categoria'))
                results = paginator.paginate_queryset(items, request)
                serializer = ItemSerializer(results, many=True, context={'request': request})
                return paginator.get_paginated_response(serializer.data)
            elif request.GET.get('producto'):
                item = Item.objects.get(slug=request.GET.get('producto'))
                serializer = ItemSerializer(item, context={'request': request})
                return Response(serializer.data)
            else:
                # pagination
                items = Item.objects.all()
                paginator = ResponsePagination()
                results = paginator.paginate_queryset(items, request)
                serializer = ItemSerializer(results, many=True, context={'request': request})
                return paginator.get_paginated_response(serializer.data)
                # items = Item.objects.all()
                # serializer = ItemSerializer(items, many=True, context={'request': request})
                # return Response(serializer.data)
    
    def post(self, request):
        if request.method == 'POST':
            print("start")
            print(request.data)
            serializer = ItemSerializer(data=request.data)
            print("A")
            if serializer.is_valid():
                print("A")
                serializer.save()
                print("C")
                # save images
                for image in request.FILES.getlist('imagenes'):
                    img = Imagen(item=serializer.instance, imagen=image)
                    img.save()
                # update serializer
                print("D")
                serializer = ItemSerializer(serializer.instance, context={'request': request})
                print("E")
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
            if request.GET.get('categoria'):
                subcategorias = Subcategoria.objects.filter(categoria=request.GET.get('categoria'))
                serializer = SubcategorySerializer(subcategorias, many=True, context={'request': request})
                return Response(serializer.data)
            serializer = SubcategorySerializer(self.get_queryset(), many=True) 
            return Response(serializer.data)
    
    def post(self, request):
        if request.method == 'POST':
            serializer = SubcategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
