from django.urls import path
from torneo.views import *

urlpatterns = [
    path('jugadores/', jugadores), 
]