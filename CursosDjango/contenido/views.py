from django.shortcuts import render, HttpResponse

# Create your views here.
menu="""
        
    <a href="/">Principal</a>
    <a href="/cursos">Cursos</a>
    <a href="/contacto">Contactanos</a>
"""

def principal(request):
    contenido="""<h1>BIENVENIDO</h1>
    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
    """
    return HttpResponse(menu+contenido)

def cursos(request):
    contenido="""
    <h2>CURSOS DISPONIBLES<h2>
    <select name="cursos" id="cursos">
    <option value="bd">Base de datos</option>
    <option value="pro">Programacion</option>
    <option value="in">Ingles</option>
    <option value="seg">Seguridad informatica</option>
    </select>
    """
    return HttpResponse(menu+contenido)

def contacto(request):
    contenido=""" 
    <h2>Contacto</h2>
    <p>Nombre: <input type="text" name="nombre"></input></p>
    <p>Correo electronico: <input type="email" name="email"></input></p>
    
    <p>Selecciona curso: </p><select name="cursos" id="cursos">
    <option value="bd">Base de datos</option>
    <option value="pro">Programacion</option>
    <option value="in">Ingles</option>
    <option value="seg">Seguridad informatica</option>
    </select>

    <p>Comentarios: </p> <p> <textarea cols="50" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="Enviar"></input></p>
    """
    return HttpResponse(menu+contenido)

