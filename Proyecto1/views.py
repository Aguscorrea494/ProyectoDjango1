from django.http import HttpResponse  # se importa django
from django.shortcuts import render # se importa el render para usar html

def saludo(response):
    return HttpResponse("Hola django")

def saludo_html(response):
    return  HttpResponse("<b>Hola django</b>")

def saludo_nombre(response, nombre):
    return HttpResponse(f"<h1>{nombre}<h1><br>Hola django")

def saludo_plantilla(request):
    contexto = {
        "nombre" : "Agustin",
        "edad": 22,
        "hijos": [
            {
                "nombre": "Sol",
                "edad": 15,
                },
            {
                "nombre": "Celi",
                "edad": 19,
                }
            ]
        }
    return render(request, template_name= "index.html", context= contexto)
