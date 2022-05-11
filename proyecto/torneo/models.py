from django.db import models

# Create your models here.

class Jugadores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField ()
    equipo = models.CharField(max_length=40)


class Equipos(models.Model):

    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=1)

class Sedes(models.Model):

    nombre = models.CharField(max_length=40)

