"""Vivieros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Vivieros import views as local_views
from apps.boards import views
#from Vivieros.views import hola, home, SINGUP, LOGIN, ABOUTUS
from Vivieros.views import  home, index
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    '''path('hello/', hola),
    path('SINGUP/', SINGUP),
    path('LOGIN/', LOGIN),
    path('ABOUTUS/', ABOUTUS),
    #path('hi/<str:name>/<int:arg>/', local_views.say_hi),
    path('posts/', views.list_posts),
    ''',
    path('', index, name='index'),
    path('', TemplateView.as_view(template='base.html')),

]
