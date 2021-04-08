from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def hola(request):
    return HttpResponse("Hola Mundo")

def home(request):
    return HttpResponse("Inicio")

def SINGUP(request):
    return HttpResponse("Registrar")

def LOGIN(request):
    return HttpResponse("Ingresar")

def ABOUTUS(request):
    return HttpResponse("Info_Viveros")

