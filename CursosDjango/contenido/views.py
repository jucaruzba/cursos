from django.shortcuts import render, HttpResponse


def principal(request):
    return render(request,"contenido/principal.html")

def cursos(request):
    return render(request,"contenido/cursos.html")
def contacto(request):
    return render(request,"contenido/contacto.html")

