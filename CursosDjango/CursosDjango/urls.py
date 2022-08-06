"""CursosDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from contenido import views
from nuevo import views as views_nuevo
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),

        path('',views_nuevo.nuevo,name="Principal"),

    path('contacto/',views_nuevo.contacto, name="Contacto"),
    path('cursos/',views.cursos, name="Cursos"),
    path('registrar/', views_nuevo.registrar, name="Registrar"),
    path('eliminarComentario/<int:id>',views_nuevo.eliminarActividadContacto,name="Eliminar"),
    path('comentarios/',views_nuevo.comentarios,name="Comentarios"),
    path('editarComentario/<int:id>/',views_nuevo.consultar,name="Consulta"),
    path("edit/<int:id>/",views_nuevo.editar, name="Editar"),
        #CONSULTAS
    path("consultas1",views_nuevo.consultar1, name="Consultas"),
    path("consultas2",views_nuevo.consultar2, name="Consultas2"),
    path("consultas3",views_nuevo.consultar3, name="Consultas3"),
    path("consultas4",views_nuevo.consultar4, name="Consultas4"),
    path("consultas5",views_nuevo.consultar5, name="Consultas5"),
    path("consultas6",views_nuevo.consultar6, name="Consultas6"),
    path("consultas7",views_nuevo.consultar7, name="Consultas7"),
    path("seguridad",views_nuevo.seguridad, name="Seguridad"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)