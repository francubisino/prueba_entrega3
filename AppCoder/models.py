from django.db import models

# Create your models here.

class Pais(models.Model):
    pais_origen=models.CharField(max_length=40)
    idioma=models.CharField(max_length=40)

class Sucursales(models.Model):
    ubicacion=models.CharField(max_length=40)
    numero=models.IntegerField()
    nombre_encargado=models.CharField(max_length=40)

class Consultas(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()    
    consulta=models.CharField(max_length=200)

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    