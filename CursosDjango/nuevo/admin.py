from django.contrib import admin
from .models import Cursos
from .models import Actividad
# Register your models here.


class AdministradorModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('indice','nombre','profesor','horario')
    search_fields=('indice','nombre','profesor','horario')
    date_hierarchy='created'
    list_filter=('profesor','horario')

admin.site.register(Cursos, AdministradorModelo)

class AdministrarActivides(admin.ModelAdmin):
    list_display=('id','actividad')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')

admin.site.register(Actividad,AdministrarActivides)