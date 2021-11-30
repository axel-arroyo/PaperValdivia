from django.db.models import query
from .models import Categoria, Item, Subcategoria, Imagen
from .serializers import ItemSerializer, CategorySerializer, SubcategorySerializer

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class ResponsePagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page'
    max_page_size = 12

# Items/Productos

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'descripcion', 'categoria__nombre', 'subcategoria__nombre', 'slug']
    pagination_class = ResponsePagination

    def get(self, request, *args, **kwargs):
        if request.GET.get('producto'):
            self.queryset = self.queryset.filter(slug=request.GET.get('producto'))
        elif request.GET.get('categoria'):
            self.queryset = Item.objects.filter(categoria__slug=request.GET.get('categoria'))
        elif request.GET.get('subcategoria'):
            self.queryset = Item.objects.filter(subcategoria__slug=request.GET.get('subcategoria'))
        return super().get(request, *args, **kwargs)


class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

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
            print("A")
            print(request.data)
            serializer = ItemSerializer(data=request.data)
            print("B")
            if serializer.is_valid():
                print("C")
                serializer.save()
                # save images
                print("D")
                for image in request.FILES.getlist('imagenes'):
                    img = Imagen(item=serializer.instance, imagen=image)
                    img.save()
                print("F")
                # update serializer
                serializer = ItemSerializer(serializer.instance, context={'request': request})
                print("G")
                return Response(serializer.data)
            print("ZZZ")
            return Response(serializer.errors)


# Categorias

class CategoryDeleteView(DestroyAPIView):
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Categoria.objects.filter(slug=self.kwargs['slug'])
    


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
