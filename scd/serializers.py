from rest_framework import serializers
from .models import  Carreras, Alumno, Docente, Administrativo, Otros


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

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'