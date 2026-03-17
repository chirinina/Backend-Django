from django.http import HttpResponse
from django.shortcuts import render

from .models import Categoria


def index(request):
    return HttpResponse("Hola mundo")

def contact(request, name):
    return HttpResponse(f"Hola {name} bienvenido a la clase de Django")

def categorias(request):
    # Captura de query params (ej.: ?nombre=PALABRA_FILTRAR)
    filtros = {
        "nombre": (request.GET.get('nombre') or "").strip()
    }

    categorias_qs = Categoria.objects.all().order_by('nombre')

    # Aplica filtro por nombre de manera insensible a mayúsculas
    if filtros["nombre"]:
        categorias_qs = categorias_qs.filter(nombre__icontains=filtros["nombre"])

    contexto = {
        "categorias": categorias_qs,
        "filtros": filtros,
        "hay_filtro": bool(filtros["nombre"]),
        "total_filtrado": categorias_qs.count(),
        "total_general": Categoria.objects.count(),
        "request": request,  # para reutilizar la ruta en el template
    }

    return render(request, 'categorias.html', contexto)
