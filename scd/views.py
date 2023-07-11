from scd.models import *
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from .models import  Alumno, Docente, Administrativo, Otros
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password


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

        
@csrf_exempt
def login_view(request):

    if request.method == 'POST':
            matricula = request.POST.get('matricula')
            password = request.POST.get('password')

            alumno = Alumno.objects.get(matricula=123456)
            #alumno = authenticate(request, matricula=matricula, password=password)
            if check_password(password, alumno.password):
                login(request, alumno)
                return JsonResponse({'message': 'Inicio de sesión exitoso.'})
            else:
                return JsonResponse({'error': 'Credenciales inválidas.'}, status=401)