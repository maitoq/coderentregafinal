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
    
    path('comentarios/lista/', ComentarioList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', ComentarioDetalle.as_view(),name='Detail'),    
    path(r'^nuevo$', ComentarioCreacion.as_view(),name='New'),    
    path(r'^editar/(?P<pk>\d+)$', ComentarioUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', ComentarioDelete.as_view(),name='Delete'),

    path('jugadores/lista/', JugadoresList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', JugadoresDetalle.as_view(),name='Detail'),    
    path(r'^nuevo$', JugadoresCreacion.as_view(),name='New'),    
    path(r'^editar/(?P<pk>\d+)$', JugadoresUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', JugadoresDelete.as_view(),name='Delete'),        
]