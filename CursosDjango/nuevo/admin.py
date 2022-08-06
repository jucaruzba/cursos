from django.contrib import admin
from .models import Cursos
from .models import Actividad
from .models import ActividadContacto
# Register your models here.


class AdministradorModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('indice','nombre','profesor','horario')
    search_fields=('indice','nombre','profesor','horario')
    date_hierarchy='created'
    list_filter=('profesor','horario')
    list_per_page=2
    list_display_links=('nombre','profesor')


    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return('matricula','carrera','turno')
        else:
            return('created','updated')

admin.site.register(Cursos, AdministradorModelo)

class AdministrarActivides(admin.ModelAdmin):
    list_display=('id','actividad')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')

admin.site.register(Actividad,AdministrarActivides)

class AdministrarActividadContacto(admin.ModelAdmin):
    list_display=('id','mensaje')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')

admin.site.register(ActividadContacto,AdministrarActividadContacto)