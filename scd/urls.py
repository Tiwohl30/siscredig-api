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
path('login/', AlumnoLoginView.as_view(), name='login'),
path('loginD/', DocenteLoginView.as_view(), name='login'),
path('loginO/', OtrosLoginView.as_view(), name='login'),
path('loginA/', AdminLoginView.as_view(), name='login'),
path('send-email/', send_email.as_view(), name='send-email'),
]

