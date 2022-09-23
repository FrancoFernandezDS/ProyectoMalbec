from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

class Variedad(models.Model):
    categoria= models.CharField(max_length=60)
    marca= models.CharField(max_length=60)
    precio= models.IntegerField()
    familia= models.CharField(max_length=50)

class Bazar(models.Model):
    tipo_de_producto = models.CharField(max_length=50)
    precio= models.IntegerField()


