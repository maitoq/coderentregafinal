import imp
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def saludo (request):
    return HttpResponse ('hola')


def prueba (request):
    diccionario = {}
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render(diccionario)
    return HttpResponse (documento)