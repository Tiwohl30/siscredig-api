from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


opciones_cuatrimestre = [
    (1, 'primer cuatrimestre'),
    (2, 'segundo cuatrimestre'),
    (3, 'tercer cuatrimestre'),
    (4, 'cuarto cuatrimestre'),
    (5, 'quinto cuatrimestre'),
    (6, 'sexto cuatrimestre'),
    (7, 'septimo cuatrimestre'),
    (8, 'octavo cuatrimestre'),
    (9, 'noveno cuatrimestre'),
    (10, 'decimo cuatrimestre'),

]

opciones_carreras = [
    ('Ingenieria de software', 'Ingenieria de software'),
    ('Ingenieria mecatronica', 'Ingenieria mecatronica'),
    ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales'),
]

parentescos = [
    ('Padre', 'Padre'),
    ('Madre', 'Madre'),
    ('Tio', 'Tio'),
    ('Tia', 'Tia'),
    ('Otro', 'Otro')
]


class AlumnoManager(BaseUserManager):
    def create_user(self, matricula, password=None, **extra_fields):
        # Crea un usuario con la matrícula y contraseña proporcionadas
        if not matricula:
            raise ValueError("La matrícula debe ser especificada.")
        
        alumno = self.model(matricula=matricula, **extra_fields)
        alumno.set_password(password)
        alumno.save(using=self._db)
        return alumno

    def create_superuser(self, matricula, password=None, **extra_fields):
        # Crea un superusuario con la matrícula y contraseña proporcionadas
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(matricula, password, **extra_fields)

class Carreras(models.Model):

    idCarrera = models.IntegerField(primary_key=True)
    nombre_carrera = models.CharField(choices=opciones_carreras, max_length=50, null=False)




class Alumno(models.Model):

    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    cuatrimestre = models.IntegerField(choices=opciones_cuatrimestre)
    fotografia = models.ImageField(null=True, upload_to='fotografias_alumnos/')
    telefono = models.CharField(max_length=13)
    carrera = models.CharField(max_length=50, choices=opciones_carreras)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    credencial_activa = models.BooleanField(default=True)
    email = models.EmailField(default='')


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'matricula'

    objects = AlumnoManager()

    def __str__(self):
        return self.email
     


class Docente(models.Model):

    
    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    email = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_docentes/')
    telefono = models.CharField(max_length=13)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    credencial_activa = models.BooleanField(default=True)


    def __str__(self):
        return self.email


class Administrativo(models.Model):


    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    email = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_administrativos/')
    telefono = models.CharField(max_length=13)
    cargo = models.CharField(max_length=20)
    area = models.CharField(max_length=30)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    credencial_activa = models.BooleanField(default=True)



    def __str__(self):
        return self.email




class Otros(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    email = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_otros/')
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    credencial_activa = models.BooleanField(default=True)

    

    def __str__(self):
        return self.email



