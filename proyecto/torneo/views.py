from django.http import HttpResponse
from django.template import loader

# Create your views here.

def jugadores (request):

    diccionario = {}
    plantilla = loader.get_template("jugadores.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

