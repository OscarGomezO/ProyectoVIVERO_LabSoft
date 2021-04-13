from django.shortcuts import render

# Create your views here.

def loginview(request):
    return render(request, 'Modulologin/baselogin.html') #Renderiza la página para ser mostrada