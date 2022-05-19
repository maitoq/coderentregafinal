from django.urls import path
from torneo.views import *

urlpatterns = [
    path('inicio/', inicio), 
    path('jugadores/', jugadores), 
    path('equipos/', equipos), 
    path('sedes/', sedes),
    path('jugadoresformulario/', jugadoresformulario), 
    path('equiposformulario/', equiposformulario), 
    path('jugadorbusqueda/', jugadorbusqueda), 
    path('buscar/', buscar),
#    path('jugadorbusquedaresultados/', jugadorbusqueda),
]