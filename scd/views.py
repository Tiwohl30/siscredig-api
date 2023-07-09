from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import AlumnoSerializer, DocenteSerializer, AdministrativoSerializer, OtrosSerializer


class LoginView(APIView):
    def post(self, request):
        correo = request.data.get('correo')
        password = request.data.get('password')
        user = authenticate(request, username=correo, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        

class RegisterView(APIView):
    def post(self, request):
        serializer = AdministrativoSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Registration successful'})
        else:
            return Response(serializer.errors, status=400)