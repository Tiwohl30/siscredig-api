from django.db import models

opciones_cuatrimestre = (
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


)

opciones_carreras = (
    ('Ingenieria de software', 'Ingenieria de software'),
    ('Ingeniería mecatronica', 'Ingeniería mecatronica'),
    ('Ingenieria en animacion y efectos visuales', 'Ingenieria en animacion y efectos visuales'),
)

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
    nombre_carrera = models.CharField(choices=opciones_carreras, max_length=120)

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
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, choices=opciones_carreras)
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia, on_delete=models.SET_NULL, null=True)
    credencial = models.ForeignKey(Credencial, on_delete=models.SET_NULL, null=True)


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
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia, on_delete=models.SET_NULL, null=True)
    credencial = models.ForeignKey(Credencial, on_delete=models.SET_NULL, null=True)
    
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
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia, on_delete=models.SET_NULL, null=True)
    credencial = models.ForeignKey(Credencial, on_delete=models.SET_NULL, null=True)

class Otros(models.Model):

    numero_control = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)
    correo = models.EmailField()
    fotografia = models.ImageField(upload_to='fotografias_otros/')
    Contacto_emergencia = models.ForeignKey(Contacto_emergencia, on_delete=models.SET_NULL, null=True)
    credencial = models.ForeignKey(Credencial, on_delete=models.SET_NULL, null=True)


    





