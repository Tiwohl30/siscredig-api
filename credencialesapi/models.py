from django.db import models

opciones_cuatrimestre = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

class Contacto_emergencia (models.Model):

    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    telefono = models.CharField(max_length=13)
    correo = models.EmailField()
    parentesco = models.CharField(max_length=15)

class Credencial(models.Model):

    folio = models.IntegerField(primary_key=True)
    codigoQR = models.ImageField(upload_to='codigos_qr/')
    fecha_inicio_vigencia = models.DateField(auto_now_add=False)
    fecha_fin_vigencia = models.DateField(auto_now_add=False)
    activa = models.BooleanField(default=True)
    contador = models.IntegerField()

class Carrera(models.Model):

    id_carerra = models.IntegerField(primary_key=True)
    nombre_carrera = models.CharField(max_length=40)

class Alumno(models.Model):

    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField(default=f"{matricula}@uptapachula.edu.mx")
    cuatrimestre = models.IntegerField(choices=opciones_cuatrimestre)
    fotografia = models.ImageField(upload_to='fotografias_alumnos/')
    telefono = models.CharField(max_length=13)
    carrera = models.ForeignKey(Carrera)
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia)
    credencial = models.ForeignKey(Credencial)


class Docente(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(upload_to='fotografias_docentes/')
    telefono = models.CharField(max_length=13)
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia)
    credencial = models.ForeignKey(Credencial)
    
class Administrativo(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(upload_to='fotografias_administrativos/')
    telefono = models.CharField(max_length=13)
    cargo = models.CharField(max_length=20)
    area = models.CharField(max_length=30)
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia)
    credencial = models.ForeignKey(Credencial)

class Otros(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(upload_to='fotografias_otros/')
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia)
    credencial = models.ForeignKey(Credencial)


    




