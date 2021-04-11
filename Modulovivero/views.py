from django.shortcuts import render

# Create your views here.

def viveroview(request):
    return render(request, 'ModuloVivero/registroviveros.html') #Renderiza la página para ser mostrada