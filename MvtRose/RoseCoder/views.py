from .models import Familia
from django.http import HttpResponse 
from django.shortcuts import render
from django.template import loader

# Create your views here.

def familia(request):
    familiar = Familia(nombre= "Rainier", apellido= "Bazan", edad= 33, pais_de_residencia ="Chile" )
    familiar.save()
    texto=f"Se guradaron los datos siguientes: nombre: {familiar.nombre}, apellido: {familiar.apellido}, edad: {familiar.edad}, pais donde reside {familiar.pais_de_residencia}"
    return HttpResponse(texto)


def familia1(request):
    familiar1 = Familia(nombre= "Mirna", apellido= "Bazan", edad= 29, pais_de_residencia ="USA" )
    familiar1.save()
    texto1=f"Se guradaron los datos siguientes: nombre: {familiar1.nombre}, apellido: {familiar1.apellido}, edad: {familiar1.edad}, pais donde reside {familiar1.pais_de_residencia}"
    return HttpResponse(texto1)

def familia2(request):
    familiar2 = Familia(nombre= "Rosseangel", apellido= "Bazan", edad= 33, pais_de_residencia ="Argentina" )
    familiar2.save()
    texto=f"Se guradaron los datos siguientes: nombre: {familiar2.nombre}, apellido: {familiar2.apellido}, edad: {familiar2.edad}, pais donde reside {familiar2.pais_de_residencia}"
    return HttpResponse(texto)




def familiares(resquest):
    
    nom= "Rainier"
    ap= "bazan"
    edad = 34
   
    diccionarios = {"nombre":nom, "apellido":ap, "edad":edad}
    plantilla = loader.get_template('Template.html')
    docu= plantilla.render(diccionarios)
    return HttpResponse(docu)








      
    


