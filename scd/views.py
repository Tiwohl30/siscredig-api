from scd.models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import  Alumno, Docente, Administrativo, Otros
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password



import logging


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')  # Obtener la contraseña del request
        if password:
            # Establecer la contraseña utilizando el método set_password
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

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
logger = logging.getLogger(__name__)

class LoginView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            alumno = Alumno.objects.get(email=email)
            if check_password(password, alumno.password):
                # Credenciales válidas
                return Response({'message': 'Autenticación exitosa'})
        except Alumno.DoesNotExist:
            pass

        # Credenciales inválidas
        return Response({'message': 'Error de autenticación'}, status=401)