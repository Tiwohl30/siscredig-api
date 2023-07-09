from scd.models import *
from rest_framework import viewsets, permissions, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Alumno, Docente, Administrativo, Otros
from django.contrib.auth import authenticate

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class AdministrativoViewSet(viewsets.ModelViewSet):
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer

class OtrosViewSet(viewsets.ModelViewSet):
    queryset = Otros.objects.all()
    serializer_class = OtrosSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarrerasSerializer

# Vistas para logins

class AlumnoLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Obtener el alumno por su correo electrónico
        try:
            alumno = Alumno.objects.get(email=email, password=password)
            
            
        except Alumno.DoesNotExist:
            return Response({'message': 'Correo invalido'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña
        if alumno.check_password(password):
            # Hacer algo si el inicio de sesión fue exitoso
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'contraseña invalida'}, status=status.HTTP_401_UNAUTHORIZED)
        

class DocenteLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Autenticar el docente utilizando el modelo de Docente
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            # Hacer algo si el inicio de sesión fue exitoso, como generar y devolver un token de autenticación
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class AdministrativoLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Autenticar el administrativo utilizando el modelo de Administrativo
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            # Hacer algo si el inicio de sesión fue exitoso, como generar y devolver un token de autenticación
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
