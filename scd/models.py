from django.db import models
import argon2

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
    nss = models.CharField(max_length=25, default=" ")
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
    password = models.CharField(max_length=128, default=" ")
    
     
    def set_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)

    def check_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False


class Docente(models.Model):

    
    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    nss = models.CharField(max_length=25, default=" ")
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


    password = models.CharField(max_length=128, default=" ")
    
     
    def set_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)

    def check_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False


class Administrativo(models.Model):


    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=13)

    password = models.CharField(max_length=128, default=" ")
    
     
    def set_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)

    def check_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False


class Otros(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nss = models.CharField(max_length=25, default=" ")
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
    cargo = models.CharField(max_length=30, default=" ")
    area = models.CharField(max_length=50, default=" ")
    telefono_contactoe = models.CharField(max_length=10, default="")
    credencial_activa = models.BooleanField(default=True)

    password = models.CharField(max_length=128, default=" ")
    
     
    def set_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)

    def check_password(self, raw_password):
        hasher = argon2.PasswordHasher()
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False
    

 