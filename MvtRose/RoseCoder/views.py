from django.http import HttpResponse 
from django.shortcuts import render
from django.template import loader
from .models import Familiares, Familias

# Create your views here.

def familias(request):

    fami1 = Familias("Roseangel", "bazan", 33 )
    fami2 = Familias ("jose","bazan",31)
    fami3 = Familias("Mirna", "bazan", 34)
    
    text1 = (f"Nombre: {fami1.nombre}, apellido: \n {fami1.ap}, edad: {fami1.edad}  ")

    text2 = (f" Nombre: {fami2.nombre}, apellido: {fami2.ap}, edad: {fami2.edad} \n ")

    text3 = (f"Nombre: {fami3.nombre}, apellido: {fami3.ap}, edad: {fami3.edad} \n ")

    text_f = (text1,text2,text3)
    return HttpResponse(text_f)



def familiares(resquest):
    
    nom= "Rainier"
    ap= "bazan"
    edad = 34
   
    diccionarios = {"nombre":nom, "apellido":ap, "edad":edad}
    plantilla = loader.get_template('Template.html')
    docu= plantilla.render(diccionarios)
    return HttpResponse(docu)











      
    


