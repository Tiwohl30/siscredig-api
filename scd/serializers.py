from rest_framework import serializers
from .models import Contacto_emergencia, Carrera, Credencial, Alumno, Docente, Administrativo, Otros

class Contacto_emergenciaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contacto_emergencia
        fields = '__all__'

class CredencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credencial
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class AdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrativo
        fields = '__all__'

class OtrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'