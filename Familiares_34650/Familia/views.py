from django.shortcuts import render

from django.http import HttpResponse

from Familia.models import Familia

# Create your views here.

def carga_de_familiar(request):
    
    Familia.objects.create(nombre = 'Emilia Leimgruber', edad = 3, trabaja = False)

    return HttpResponse('Se cargo un familiar')

def lista_de_familiares(request):
    all_familiares = Familia.objects.all()
    context = {'familiares': all_familiares}

    return render(request,'listado_de_familiares.html', context = context)
