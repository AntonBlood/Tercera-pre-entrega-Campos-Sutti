from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.IntegerField()
    
    
class Compra(models.Model):
    cantidad=models.IntegerField()
    producto=models.CharField(max_length=20)