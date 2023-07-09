from rest_framework import routers
from django.urls import path, include
from .views import *


from . import views

# Definir el enrutador existente
router = routers.DefaultRouter()


router.register(r'alumnos', AlumnoViewSet, 'alumnos')

router.register(r'docentes', DocenteViewSet, 'docentes')

router.register(r'administrativos', AdministrativoViewSet, 'administrativos')

router.register(r'otros', OtrosViewSet, 'otros')

router.register(r'carrera', CarreraViewSet, 'carrera')


urlpatterns = [

path('api/', include(router.urls)),
path('api/alumno/login/', views.AlumnoLoginView.as_view(), name='alumno_login'),
path('api/docente/login/', views.DocenteLoginView.as_view(), name='docente_login'),
path('api/administrativo/login/', views.AdministrativoLoginView.as_view(), name='administrativo_login'),


]

