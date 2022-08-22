from urllib import request
from django.db import models


# Create your models here.#modelos
#mi clase modelo

class Familia(models.Model):
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(default=1)
    pais_de_residencia = models.CharField(max_length=30)



    
    
