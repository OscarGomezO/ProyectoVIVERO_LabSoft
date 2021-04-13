from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from Modulovivero import views

urlpatterns = [
    path('', views.viveroview, name='viverohome'),
    path('registrovivero/', views.viveroview, name='registro_vivero'),
    path('registrousuario/', views.usuarioview, name='registro_usuario'),
    path('registroproductoscontrol/', views.productocontrolview, name='registro_productocontrol'),
    path('registrolabor/', views.laborview, name='registro_labor'),
    path('contacto/', views.contactoview, name='info_contacto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)