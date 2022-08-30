from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse

# Create your views here.

def familiar(request):
    familiar1=Familiares(nombre="cristiano", apellido="ronaldo",telefono=5555555,anio_nacimiento="1990-05-11")
    familiar1.save()
    texto1=f"Familiar Creado: nombre: {familiar1.nombre} apellido: {familiar1.apellido} telefono: {familiar1.telefono} año de nacimiento: {familiar1.anio_nacimiento}"
#    texto="Familiar"
    familiar2=Familiares(nombre="samuel", apellido="eto",telefono=4444444,anio_nacimiento="1983-12-10")
    familiar2.save()
    texto2=f"Familiar Creado: nombre: {familiar2.nombre} apellido: {familiar2.apellido} telefono: {familiar2.telefono} año de nacimiento: {familiar2.anio_nacimiento}"
#    texto="Familiar"
    familiar3=Familiares(nombre="ricardo", apellido="montaner",telefono=444444444,anio_nacimiento="1960-03-29")
    familiar3.save()
    texto3=f"Familiar Creado: nombre: {familiar3.nombre} apellido: {familiar3.apellido} telefono: {familiar3.telefono} año de nacimiento: {familiar3.anio_nacimiento}"
#    texto="Familiar"
    texto=f"familiar 1: {texto1} \n familiar 2: {texto2} \nfamiliar 3: {texto3}"
    return HttpResponse(texto)