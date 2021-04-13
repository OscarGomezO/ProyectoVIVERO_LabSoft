from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from Modulologin import views

rlpatterns = [
    #path('', views.viveroview, name='viverohome'),
    path('login/', views.loginview, name='login_vivero'),
    #path('registrovivero/', views.viveroview, name='registro_vivero'),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)