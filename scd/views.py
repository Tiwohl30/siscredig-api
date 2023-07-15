from scd.models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import  Alumno, Docente, Administrativo, Otros
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect





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

    def perform_create(self, serializer):
        password = self.request.data.get('password')  # Obtener la contraseña del request
        if password:
            # Establecer la contraseña utilizando el método set_password
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

class AdministrativoViewSet(viewsets.ModelViewSet):
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')  # Obtener la contraseña del request
        if password:
            # Establecer la contraseña utilizando el método set_password
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

class OtrosViewSet(viewsets.ModelViewSet):
    queryset = Otros.objects.all()
    serializer_class = OtrosSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')  # Obtener la contraseña del request
        if password:
            # Establecer la contraseña utilizando el método set_password
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarrerasSerializer

# Vistas para logins
logger = logging.getLogger(__name__)

class AlumnoLoginView(APIView):
    
    def post(self, request):
        matricula = request.data.get('matricula')
        password = request.data.get('password')

        try:
            alumno = Alumno.objects.get(matricula=matricula)
            if check_password(password, alumno.password):
                # Credenciales válidas
                return Response({'message': 'Autenticación exitosa'})
        except Alumno.DoesNotExist:
            pass

        # Credenciales inválidas
        return Response({'message': 'Error de autenticación'}, status=401)
    

class DocenteLoginView(APIView):
    
    def post(self, request):
        numero_control = request.data.get('numero_control')
        password = request.data.get('password')

        try:
            docente = Docente.objects.get(numero_control=numero_control)
            if check_password(password, docente.password):
                # Credenciales válidas
                return Response({'message': 'Autenticación exitosa'})
        except Docente.DoesNotExist:
            pass

        # Credenciales inválidas
        return Response({'message': 'Error de autenticación'}, status=401)
    

class OtrosLoginView(APIView):
    
    def post(self, request):

        numero_control = request.data.get('numero_control')
        password = request.data.get('password')

        try:
            otros = Otros.objects.get(numero_control=numero_control)
            if check_password(password, otros.password):
                # Credenciales válidas
                return Response({'message': 'Autenticación exitosa'})
        except Otros.DoesNotExist:
            pass

        # Credenciales inválidas
        return Response({'message': 'Error de autenticación'}, status=401)
    
class AdminLoginView(APIView):
    
    def post(self, request):

        numero_control = request.data.get('numero_control')
        password = request.data.get('password')

        try:
            admin = Administrativo.objects.get(numero_control=numero_control)
            if check_password(password, admin.password):
                # Credenciales válidas
                return Response({'message': 'Autenticación exitosa'})
        except Administrativo.DoesNotExist:
            pass

        # Credenciales inválidas
        return Response({'message': 'Error de autenticación'}, status=401)
    

class send_email(APIView):

    def post(self, request):

        destinatario = request.data.get('destinatario')
        asunto = request.data.get('asunto')
        contenido = request.data.get('contenido')
        remitente = '221025@uptapachula.edu.mx'

        if destinatario and contenido and remitente:
            try:
                send_mail(asunto, contenido, remitente, [destinatario])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return Response({'message': 'enviado'})
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse("Make sure all fields are entered and valid.")