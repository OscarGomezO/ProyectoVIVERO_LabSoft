from django.shortcuts import render

#Creamos las vistas
def home(request):
    return render(request, 'Modulovivero/index.html') #Accedemos a la ruta por medio de la URL #vivero es el name de la URL de ProyectoVIVERO_LabSoft