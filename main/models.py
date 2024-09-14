from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)
    # direccion (viene del related_name)
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    # Se omitió el campo depto
    comuna = models.CharField(max_length=50, null=False)
    # Se omitió el campo región
    region = models.CharField(max_length=50, null=False)
    estudiante = models.OneToOneField(  
        Estudiante,
        related_name='direccion',
        on_delete=models.CASCADE
    )

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)


class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    version = models.IntegerField()
    profesor = models.ManyToManyField(
        Profesor, 
        related_name='cursos', 
       
    )
    estudiante = models.ManyToManyField(
        Estudiante, 
        related_name='cursos',
        
    )