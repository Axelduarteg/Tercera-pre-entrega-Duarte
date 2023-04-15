from django.urls import path
from .views import *

urlpatterns = [
    path("",inicioapp, name="inicioapp"),
    path("crear_curso/", crear_curso),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("buscarEstudiante/", buscarEstudiante, name="buscarEstudiante"),
    path("buscandoEstudiante/", buscandoEstudiante, name="buscandoEstudiante"),
]