from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Cursos

def nuevo(request):
    cursos=Cursos.objects.all()

    return render(request,"nuevo/principal.html", {"cursos":cursos})