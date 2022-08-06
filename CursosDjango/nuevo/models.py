from sre_parse import Verbose
from django.db import models

from ckeditor.fields import RichTextField

class Cursos(models.Model): #Define la estructura de nuestra tabla
    indice = models.CharField(max_length=12, verbose_name="Identificador")
    nombre = models.TextField(verbose_name="Nombre") #Texto
    profesor = models.TextField(verbose_name="Profesor")
    horario= models.TextField(max_length=10, verbose_name="Horario")
    numAlumnos=models.SmallIntegerField(verbose_name="Alumnos")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"
        ordering=["created"] #Este elemento indica que se ordernara del más recienre al ,mas viejo
        
    def __str__(self):
        return self.nombre #Indica que se mostrare el nombre en la tabla 

class Actividad(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    curso=models.ForeignKey(Cursos,
        on_delete=models.CASCADE, verbose_name="Curso")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    actividad=RichTextField(verbose_name="Actividad")

    class Meta:
        verbose_name="Actividad"
        verbose_name_plural="Actividades"
        ordering=["-created"]

    def __str__(self):
        return self.actividad


class ActividadContacto(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.TextField(verbose_name="Usuario")
    mensaje=models.TextField(verbose_name="Comentario")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contactos"
        ordering=["-created"]

    def __str__(self):
        return self.mensaje