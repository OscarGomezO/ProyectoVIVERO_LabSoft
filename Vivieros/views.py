from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response



"""
def hola(request):
    return HttpResponse("Hola Mundo")
def SINGUP(request):
    return HttpResponse("Registrar")

def LOGIN(request):
    return HttpResponse("Ingresar")

def ABOUTUS(request):
    return HttpResponse("Info_Viveros")
"""
def home(request):
    return HttpResponse("Inicio")

def index(request):
    return render_to_response('base.html')



