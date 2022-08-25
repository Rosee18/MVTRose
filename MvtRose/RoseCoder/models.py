from pyexpat import model
from urllib import request
from django.db import models


# Create your models here.#modelos
#mi clase modelo

class Familiares(models.Model):
        

    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(default=1)
    pais_de_residencia = models.CharField(max_length=30)
    fn= models.DateTimeField()


#Nueva clase agregada
class Familias:
    def __init__(self,nombre,ap,edad) -> None:

        self.nombre = nombre
        self.ap = ap
        self.edad = edad





    
    
