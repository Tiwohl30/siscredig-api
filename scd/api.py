from scd.models import *
from rest_framework import viewsets, permissions
from .serializers import *
from .models import  Alumno, Docente, Administrativo, Otros


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
    