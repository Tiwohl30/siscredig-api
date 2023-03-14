from scd.models import *
from rest_framework import viewsets, permissions
from .serializers import *
from .models import Contacto_emergencia, Credencial, Alumno, Docente, Administrativo, Otros


class ContactoEmergenciaViewSet(viewsets.ModelViewSet):
    queryset = Contacto_emergencia.objects.all()
    serializer_class = Contacto_emergenciaSerializer

class CredencialViewSet(viewsets.ModelViewSet):
    queryset = Credencial.objects.all()
    serializer_class = CredencialSerializer

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
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
    