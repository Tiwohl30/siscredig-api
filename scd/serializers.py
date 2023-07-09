from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Carreras, Alumno, Docente, Administrativo, Otros



class AlumnoSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Alumno.objects.create_user(user_type='Alumno', **validated_data)
        return user

    class Meta:
        model = Alumno
        fields = ['username', 'password']


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'


class AdministrativoSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Administrativo.objects.create_user(correo=validated_data['correo'], password=validated_data['password'])
        return user

    class Meta:
        model = Administrativo
        fields = ['correo', 'password']

class OtrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = '__all__'

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'