from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *
# Create your views here.

def crear_curso(request):
    
    nombre_curso="Python"
    comision_curso=51325
    print("Creando Curso")
    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado--- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def cursos(request):
    
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso()
            curso.nombre = form.cleaned_data["nombre"]
            curso.comision = form.cleaned_data["comision"]
            curso.save()
            form = CursoForm()
    else:
        form = CursoForm()
        
    cursos = Curso.objects.all()
    context = {"cursos": cursos, "form" : form}
    return render(request,"Appcoder/cursos.html", context)

def profesores(request):
    
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data["nombre"]
            profesor.apellido = form.cleaned_data["apellido"]
            profesor.email = form.cleaned_data["email"]
            profesor.profesion = form.cleaned_data["profesion"]
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all()
    context = {"profesores": profesores, "form" : form}
    return render(request,"Appcoder/profesores.html", context)

def editarProfesor(request, id):
    profesor= Profesor.objects.get(id=id)
    if request.method=="POST":
        form= ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, "Appcoder/Profesores.html", {"profesores": profesores, "mensaje":"profesor editado corectamente"})
        pass
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "Appcoder/profeFormulario.html", {"form": formulario, "profesor":profesor})            

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form = ProfesorForm()
    return render (request,"Appcoder/Profesores.html", {"profesores": profesores, "mensaje":"profesor eliminado corectamente", "form": form})

def estudiantes(request):
    
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            Estudiantes = Estudiante()
            Estudiantes.nombre = form.cleaned_data["nombre"]
            Estudiantes.apellido = form.cleaned_data["apellido"]
            Estudiantes.email = form.cleaned_data["email"]
            Estudiantes.save()
            form = EstudianteForm()
    else:
        form = EstudianteForm()
        
    estudiantes = Estudiante.objects.all()
    context = {"estudiantes": estudiantes, "form" : form}
    return render(request,"Appcoder/estudiantes.html", context)

def entregables(request):
        
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            Entregables = Entregable()
            Entregables.nombre = form.cleaned_data["nombre"]
            Entregables.fecha_entrega = form.cleaned_data["fecha_entrega"]
            Entregables.entregado = form.cleaned_data["entregado"]
            Entregables.save()
            form = EntregableForm()
    else:
        form = EntregableForm()

    entregables = Entregable.objects.all()
    context = {"entregables": entregables, "form" : form}
    return render(request,"Appcoder/entregables.html", context)

def inicio(request):
    return HttpResponse("Bienvenido")

def inicioapp(request):
    return render(request,"Appcoder/inicio.html")
    
def buscarEstudiante(request):
    return render(request, "Appcoder/busquedaEstudiante.html")
    
def buscandoEstudiante(request):
    apellidoIngresado= request.GET["apellido"]
    if apellidoIngresado!="":
        estudiantes=Estudiante.objects.filter(apellido__icontains=apellidoIngresado)
        print(estudiantes)
        return render(request, "Appcoder/resultadosBusquedaEstudiantes.html", {"estudiantes": estudiantes})
    else:
        return render(request, "Appcoder/busquedaEstudiante.html", {"mensaje": "No as ingresado un apellido para buscar"})

def busquedaComision(request):
    return render(request,"Appcoder/busquedaComision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos=Curso.filter(comision__icontains=comision)
        return render(request, "Appcoder/busquedaComision.html", {"cursos": cursos})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje": "Ingresa una comision para buscar"})