from django.db import models
from django.contrib.auth.models import User

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
    imagen = models.ImageField(upload_to="bebidas", null=True, blank= True)

class Bazar(models.Model):
    tipo_de_producto = models.CharField(max_length=50)
    precio= models.IntegerField()
    imagen = models.ImageField(upload_to="bazar", null=True,blank= True)

class Avatar(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null= True, blank= True)

