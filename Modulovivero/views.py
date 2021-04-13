from django.shortcuts import render

# Create your views here.

def viveroview(request):
    return render(request, 'ModuloVivero/registroviveros.html') #Renderiza la página para ser mostrada

def usuarioview(request):
    return render(request, 'ModuloVivero/registrousuarios.html')

def productocontrolview(request):
    return render(request, 'ModuloVivero/registrocontrol.html')

def laborview(request):
    return render(request, 'ModuloVivero/registrolabor.html')

def contactoview(request):
    return render(request, 'static/contact.html')