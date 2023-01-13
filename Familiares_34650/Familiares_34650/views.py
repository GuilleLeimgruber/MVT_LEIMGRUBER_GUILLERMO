from django.http import HttpResponse
from django.shortcuts import render


def pagina_de_bienvenida(request):

 return HttpResponse('Bienvenidos a la pagina de Inicio')

def familiar_de_prueba(request):
    
    prueba = {'Nombre': 'Guillermo', 'Edad': 43, 'Curso': 'Python'}
 
    context = {'familiar': prueba}
    return render(request, 'familiar_prueba.html', context = context)

    