from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('inicio/', inicio, name="Entrega1-inicio"),
    path('Jugadores/', jugadores, name="Entrega1-jugadores"),
    path('Jugadores/agregar/', agregar_jugador, name="Entrega1-agregar-jugador"),
    path('Jugadores/buscar/', buscar_jugador, name="Entrega1-buscar-jugador"),
    path('Jugadores/buscar/resultado/', resultados_busqueda_jugador, name="Entrega1-resultado-jugador"),

    #----------------------------------------------------------------------

    path('Equipos/', equipos, name="Entrega1-Equipos"),
    path('Equipos/agregar/', agregar_equipo, name="Entrega1-agregar-equipo"),
    path('Equipos/buscar/', buscar_equipo, name="Entrega1-buscar-Equipos"),
    path('Equipos/buscar/resultado/', resultados_busqueda_equipo, name="Entrega1-resultado-Equipos"),

      #----------------------------------------------------------------------
      
    path('Estadios/', estadios, name="Entrega1-Estadios"),
    path('Estadios/agregar/', agregar_estadio, name="Entrega1-agregar-Estadios"),
    path('Estadios/buscar/', buscar_estadio, name="Entrega1-buscar-Estadios"),
    path('Estadios/buscar/resultado/', resultados_busqueda_estadio, name="Entrega1-resultado-Estadios"),
]