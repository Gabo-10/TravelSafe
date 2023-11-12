from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

         # Create your models here.

# class Genero(models.Model):
#     idGenero = models.IntegerField(primary_key=True, db_column='idGenero')
#     tipoGenero = models.CharField(max_length=100,db_column='tipoGenero')
#     class Meta:
#         db_table='Genero'
        
# class Alumno(models.Model):
#     idAlumnos = models.IntegerField(primary_key=True,db_column='idAlumno')
#     nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
#     fk_genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
#     class Meta:
#         db_table='Alumnos'
        
# class Alumno_has_Genero(models.Model):
#     fk_Alumno = models.ForeignKey(Alumno,default=1,on_delete=models.CASCADE,db_column='fk_alumno')
#     fk_Genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
#     class Meta:
#         db_table='alumno_has_genero'


class Usuarios(models.Model):
    idUsuarios = models.IntegerField(primary_key=True, db_column='id')
    usuario = models.CharField(max_length=100,db_column='usuario')
    contraseña = models.CharField(max_length=100,db_column='contraseña')
    correo = models.CharField(max_length=100,db_column='correo')
    # matricula = models.CharField(max_length=100,db_column='matricula')
    class Meta:
        db_table='Usuarios'
        
        
class Encuesta(models.Model):
    correo = models.CharField(max_length=100, db_column='correo')
    nombre = models.CharField(max_length=100, db_column='nombre')
    pregun1 = models.CharField(max_length=100, db_column='pregun1')
    pregun2 = models.CharField(max_length=100, db_column='pregun2')
    pregun3 = models.CharField(max_length=100, db_column='pregun3')
    pregun4 = models.CharField(max_length=100, db_column='pregun4')
    pregun5 = models.CharField(max_length=100, db_column='pregun5')
    pregun6 = models.CharField(max_length=100, db_column='pregun6')
    pregun7 = models.CharField(max_length=100, db_column='pregun7')
    pregun8 = models.CharField(max_length=100, db_column='pregun8')
    pregun9 = models.CharField(max_length=100, db_column='pregun9')
    pregun10 = models.CharField(max_length=100, db_column='pregun10')
    class Meta:
        db_table='formula'