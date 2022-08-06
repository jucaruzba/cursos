from django.shortcuts import render
from .forms import ActividadContactoForm
from .models import ActividadContacto, Cursos
import datetime
from django.shortcuts import get_object_or_404

def nuevo(request):
    cursos=Cursos.objects.all()

    return render(request,"nuevo/principal.html", {"cursos":cursos})

def comentarios(request):
    comentarios=ActividadContacto.objects.all()
    return render(request,"nuevo/comentarios.html",{"comentarios":comentarios})

def registrar(request):
    if request.method == 'POST':
        form=ActividadContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ActividadContacto.objects.all()
            return render(request,'nuevo/comentarios.html',{"comentarios":comentarios})

    form=ActividadContactoForm()
    return render(request,'nuevo/contacto.html',{'form':form})


def contacto(request):
    return render(request,"nuevo/contacto.html")

def eliminarActividadContacto(request, id,confirmacion='nuevo/confirmarEliminacion.html'):
    comentario=get_object_or_404(ActividadContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ActividadContacto.objects.all()
        return render(request,'nuevo/comentarios.html',{"comentarios":comentarios})
    return render(request,confirmacion,{'object':object})

def consultar(request, id):
    comentario=ActividadContacto.objects.get(id=id)
    return render(request,"nuevo/editarComentario.html",{'comentario':comentario})  

def editar(request,id):
    comentario=get_object_or_404(ActividadContacto, id=id)
    form=ActividadContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ActividadContacto.objects.all()
        return render(request,'nuevo/comentarios.html',{"comentarios":comentarios})
    return render(request,"nuevo/editarComentario.html",{'comentario':comentario})  


##CONSULTAS

def consultar1(request):
    cursos=Cursos.objects.filter(nombre="Seguiridad Informatica")
    return render(request,"nuevo/consultas.html", {"cursos":cursos})

def consultar2(request):
    cursos=Cursos.objects.filter(nombre="Seguiridad Informatica").filter(horario="Matutino")
    return render(request,"nuevo/consultas.html", {"cursos":cursos})

def consultar3(request):
    cursos=Cursos.objects.all().only("nombre","profesor","horario","imagen")
    return render(request,"nuevo/consultas.html", {"cursos":cursos})

def consultar4(request):
    cursos=Cursos.objects.filter(turno__contains="Vesp")
    return render(request,"nuevo/consultas.html", {"cursos":cursos})

def consultar5(request):
    cursos=Cursos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"nuevo/consultas.html", {"cursos":cursos})


def consultar6(request):
    fechaInicio=datetime.date(2022, 7, 1)
    fechaFin=datetime.date(2022,7,14)
    cursos=Cursos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"nuevo/consultas.html", {"cursos":cursos})


def consultar7(request):
    cursos=Cursos.objects.filter(comentario__coment__contains="trabajo")
    return render(request,"nuevo/consultas.html", {"cursos":cursos})


def seguridad(request, nombre=None):
    nombre=request.GET.get('nombre')
    return render(request,"nuevo/seguridad.html",{'nombre':nombre})