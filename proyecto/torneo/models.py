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

class Comentario(models.Model):

    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    imagen = models.ImageField()