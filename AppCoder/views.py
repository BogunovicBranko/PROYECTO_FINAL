from django.shortcuts import render
from AppCoder.models import *



def inicio(request):


    return render(request, "AppCoder/index.html")

def jugadores(request):
    jugadores = Jugadores.objects.all()

    return render(request, "AppCoder/jugadores.html", {"jugadores":jugadores})

def agregar_jugador(request):

    if request.method == "POST":
        nombre_jugador = request.POST["nombre"]
        apellido_jugador = request.POST["apellido"]
        fecnac_jugador = request.POST["fecnac"]
        Equipo_jugador = request.POST["Equipo"]

        jugador = Jugadores(nombre=nombre_jugador, apellido=apellido_jugador, fecnac=fecnac_jugador, Equipo=Equipo_jugador)
        jugador.save()
    return render(request, "AppCoder/Agregar_jugador.html")

def buscar_jugador(request):

    return render(request, "AppCoder/busqueda_jugador.html" )

def resultados_busqueda_jugador(request):
    nombre_jugador = request.GET["nombre"]
    jugadores = Jugadores.objects.filter(nombre__icontains=nombre_jugador)
    return render(request, "AppCoder/resultados_busqueda_jugador.html", {"jugadores":jugadores})

    
#--------------------------------------------------------------------------------------------------------------

def equipos(request):
    equipos = Equipos.objects.all()

    return render(request, "AppCoder/Equipos.html", {"equipos":equipos})


def agregar_equipo(request):

    if request.method == "POST":
        nombre_equipo = request.POST["nombre"]
        colorcamiseta_equipo = request.POST["colorcamiseta"]
        totaljugadores_equipo = request.POST["totaljugadores"]

        equipo = Equipos(nombre=nombre_equipo, colorcamiseta=colorcamiseta_equipo, totaljugadores=totaljugadores_equipo)
        equipo.save()
    return render(request, "AppCoder/Agregar_equipo.html")

def buscar_equipo(request):

    return render(request, "AppCoder/busqueda_equipo.html" )

def resultados_busqueda_equipo(request):
    nombre_equipo = request.GET["nombre"]
    equipo = Equipos.objects.filter(nombre__icontains=nombre_equipo)
    return render(request, "AppCoder/resultados_busqueda_equipo.html", {"equipos":equipo})

    #------------------------------------------------------------------------------------------------------------

def estadios(request):
    estadios = Estadios.objects.all()

    return render(request, "AppCoder/Estadios.html", {"estadios":estadios})


def agregar_estadio(request):

    if request.method == "POST":
        nombre_estadio = request.POST["nombre"]
        Capacidad_estadio = request.POST["Capacidad"]

        estadio = Estadios(nombre=nombre_estadio, Capacidad=Capacidad_estadio)
        estadio.save()
    return render(request, "AppCoder/Agregar_estadio.html")

def buscar_estadio(request):

    return render(request, "AppCoder/busqueda_estadio.html" )

def resultados_busqueda_estadio(request):
    nombre_estadio = request.GET["nombre"]
    estadios = Estadios.objects.filter(nombre__icontains=nombre_estadio)
    return render(request, "AppCoder/resultados_busqueda_estadio.html", {"estadios":estadios})

# Create your views here.
