from django.db import models

class Jugadores(models.Model):
  nombre = models.CharField(max_length=40)
  apellido = models.CharField(max_length=40)
  fecnac = models.DateField()
  Equipo = models.CharField(max_length=40)

class Equipos(models.Model):
  nombre = models.CharField(max_length=40)
  colorcamiseta = models.CharField(max_length=40)
  totaljugadores = models.IntegerField()

class Estadios(models.Model):
  nombre = models.CharField(max_length=40)
  Capacidad = models.IntegerField()

# Create your models here.
