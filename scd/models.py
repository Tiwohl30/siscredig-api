from django.db import models
from django.contrib.auth.hashers import make_password, check_password

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
    correo = models.EmailField(default=f"{matricula}@uptapachula.edu.mx")
    cuatrimestre = models.IntegerField(choices=opciones_cuatrimestre)
    fotografia = models.ImageField(null=True, upload_to='fotografias_alumnos/')
    telefono = models.CharField(max_length=13)
    carrera = models.CharField(max_length=50, choices=opciones_carreras)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=128, default=f"{matricula}")
    credencial_activa = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)



class Docente(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_docentes/')
    telefono = models.CharField(max_length=13)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=128, default=f"{numero_control}")
    credencial_activa = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)



class Administrativo(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_administrativos/')
    telefono = models.CharField(max_length=13)
    cargo = models.CharField(max_length=20)
    area = models.CharField(max_length=30)
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=128, default="nimda")
    credencial_activa = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)




class Otros(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(null=True, upload_to='fotografias_otros/')
    nombre_contactoe = models.CharField(max_length=20, default="")
    apellido_paterno_contactoe = models.CharField(max_length=20, default="")
    apellido_materno_contactoe = models.CharField(max_length=20, default="")
    parentescto_contactoe = models.CharField(max_length=15, choices=parentescos, default="")
    telefono_contactoe = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=128, default=f"{numero_control}")
    credencial_activa = models.BooleanField(default=True)


    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    





