from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/contactos', ContactoEmergenciaViewSet, 'contactoEmergencia')

router.register('api/credenciales', CredencialViewSet, 'credenciales')

router.register('api/alumnos', AlumnoViewSet, 'alumnos')

router.register('api/docentes', DocenteViewSet, 'docentes')

router.register('api/administrativos', AdministrativoViewSet, 'administrativos')

router.register('api/otros', OtrosViewSet, 'otros')

router.register('api/carrera', CarreraViewSet, 'carrera')

urlpatterns = router.urls

