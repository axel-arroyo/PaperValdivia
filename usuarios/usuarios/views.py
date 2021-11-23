from .models import Usuario
from .serializers import LoginSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token


class UserView(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        if request.method == 'GET':
            if request.GET.get('correo'):
                usuarios = Usuario.objects.filter(correo=request.GET.get('correo'))
                serializer = UserSerializer(usuarios)
                return Response(serializer.data)
            else:
                usuarios = Usuario.objects.all()
                serializer = UserSerializer(usuarios, many=True)
                return Response(serializer.data)


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            account = serializer.save()
            data = serializer.data
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data)
        return Response(serializer.errors)

@api_view(['POST',])
def login_view(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'nombre': user.nombre, 'is_staff': user.is_staff})
