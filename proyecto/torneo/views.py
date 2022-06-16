from ast import Del
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

def about (request):

    diccionario = {}
    plantilla = loader.get_template("about.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def comentarios (request):

    diccionario = {}
    plantilla = loader.get_template("comentarios.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def contact (request):

    diccionario = {}
    plantilla = loader.get_template("sinpagina.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def termsofuse (request):

    diccionario = {}
    plantilla = loader.get_template("sinpagina.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def privacypolicy (request):

    diccionario = {}
    plantilla = loader.get_template("sinpagina.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def enconstruccion (request):

    diccionario = {}
    plantilla = loader.get_template("sinpagina.html")
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

        if miFormulario.is_valid():
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

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            equipo = Equipos (nombre=informacion['nombre'],categoria=informacion['categoria'])
            equipo.save()
            return render(request,'torneo/inicio.html')
    else:
        miFormulario = EquiposFormulario()
    
    return render(request,'torneo/equiposformulario.html',{"miFormulario":miFormulario})

def sedesformulario (request):
    if request.method == 'POST':
        miFormulario = SedesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            sede = Sedes (nombre=informacion['nombre'])
            sede.save()
            return render(request,'torneo/inicio.html')
    else:
        miFormulario = SedesFormulario()
    
    return render(request,'torneo/sedesformulario.html',{"miFormulario":miFormulario})

#----------------------------------- búsqueda ---------------------------

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

#--------------------------------------------------------------------
def listacomentarios (request):
    comentarios = Comentario.objects.all()
    return render(request,'torneo/listacomentarios.html',{"comentarios":comentarios})

#-------------------------------------------------------------------
#CRUD con clases basadas en vistas
#comentarios

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ComentarioList (ListView):
    model = Comentario
    template_name = 'torneo/comentarioslista.html'

class ComentarioDetalle (DetailView):
    model = Comentario
    template_name = 'torneo/comentariosdetalle.html'

class ComentarioCreacion (CreateView):
    model = Comentario
    success_url = '/torneo/comentarios/lista/'
    fields = ['titulo','subtitulo','cuerpo','autor','fecha']

class ComentarioUpdate (UpdateView):
    model = Comentario
    success_url = '/torneo/comentarios/lista/'
    fields = ['titulo','subtitulo','cuerpo','autor','fecha']    

class ComentarioDelete (DeleteView):
    model = Comentario
    success_url = '/torneo/comentarios/lista/'

#jugadores

class JugadoresList (ListView):
    model = Jugadores
    template_name = 'torneo/jugadoreslista.html'

class JugadoresDetalle (DetailView):
    model = Jugadores
    template_name = 'torneo/jugadoresdetalle.html'

class JugadoresCreacion (CreateView):
    model = Jugadores
    success_url = '/torneo/Jugadores/lista/'
    fields = ['nombre','apellido','edad','equipo']

class JugadoresUpdate (UpdateView):
    model = Jugadores
    success_url = '/torneo/Jugadores/lista/'
    fields = ['nombre','apellido','edad','equipo']

class JugadoresDelete (DeleteView):
    model = Jugadores
    success_url = '/torneo/Jugadores/lista/'