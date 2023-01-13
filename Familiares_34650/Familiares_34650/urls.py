"""Familiares_34650 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Familiares_34650.views import pagina_de_bienvenida, familiar_de_prueba
from Familia.views import carga_de_familiar, lista_de_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina_de_inicio/', pagina_de_bienvenida),
    path('prueba/', familiar_de_prueba),
    path('carga_de_familiar/', carga_de_familiar),
    path('lista_de_familiares/', lista_de_familiares),
]
