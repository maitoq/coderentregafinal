from django.urls import path
from torneo.views import *

urlpatterns = [
    path('', inicio), 
    path('inicio/', inicio), 
    path('jugadores/', jugadores), 
    path('equipos/', equipos), 
    path('sedes/', sedes),
    path('jugadoresformulario/', jugadoresformulario), 
    path('equiposformulario/', equiposformulario), 
    path('sedesformulario/', sedesformulario),
    path('jugadorbusqueda/', jugadorbusqueda), 
    path('buscar/', buscar),
#    path('jugadorbusquedaresultados/', jugadorbusqueda),
    path('about/', about),
    path('contact/', contact),
    path('termsofuse/', termsofuse),
    path('privacypolicy/', privacypolicy),
    path('enconstruccion/', enconstruccion),
    path('comentarios/', listacomentarios),
    
]