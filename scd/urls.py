from rest_framework import routers
from .api import *
from django.urls import path, include
from .views import LoginView, RegisterView
from . import views

# Definir el enrutador existente
router = routers.DefaultRouter()
# Agregar más rutas para otros modelos si es necesario



router.register('api/alumnos', AlumnoViewSet, 'alumnos')

router.register('api/docentes', DocenteViewSet, 'docentes')

router.register('api/administrativos', AdministrativoViewSet, 'administrativos')

router.register('api/otros', OtrosViewSet, 'otros')

router.register('api/carrera', CarreraViewSet, 'carrera')


urlpatterns = [
    # URLs del enrutador existente
    path('api/', include(router.urls)),
    
    # URL para el inicio de sesión
    path('api/login/', LoginView.as_view(), name='login'),
    
    # URL para el registro
    path('api/register/', RegisterView.as_view(), name='register'),
    
    # Otras URLs adicionales si es necesario
]

