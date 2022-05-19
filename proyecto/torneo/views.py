from django.http import HttpResponse
from django.template import loader
from torneo.forms import *
from torneo.models import *
from django.shortcuts import render

# Create your views here.

def inicio (request):

    diccionario = {}
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def jugadores (request):
    diccionario = {}
    plantilla = loader.get_template("jugadores.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def equipos (request):
    diccionario = {}
    plantilla = loader.get_template("equipos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def sedes (request):
    diccionario = {}
    plantilla = loader.get_template("sedes.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def jugadoresformulario (request):
    if request.method == 'POST':
        miFormulario = JugadoresFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            jugador = Jugadores (nombre=informacion['nombre'],apellido=informacion['apellido'],edad=informacion['edad'],equipo=informacion['equipo'])
            jugador.save()
            return render(request,'torneo/inicio.html')
    else:
        miFormulario = JugadoresFormulario()
    
    return render(request,'torneo/jugadoresformulario.html',{"miFormulario":miFormulario})


def equiposformulario (request):
    if request.method == 'POST':
        miFormulario = EquiposFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            equipo = Equipos (nombre=informacion['nombre'],categoria=informacion['categoria'])
            equipo.save()
            return render(request,'torneo/inicio.html')
    else:
        miFormulario = EquiposFormulario()
    
    return render(request,'torneo/equiposformulario.html',{"miFormulario":miFormulario})

def jugadorbusqueda (request):
    return render (request,'torneo/jugadorbusqueda.html')

def buscar (request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        jugadores = Jugadores.objects.filter(apellido__icontains=apellido)
        return render(request,'torneo/jugadorbusquedaresultados.html',{"jugadores":jugadores,"apellido":apellido})
    
    else:
        respuesta = "sin datos"
    
    return HttpResponse(respuesta)