from django.http import HttpResponse
from django.shortcuts import render

from .models import Categoria

def categorias(request):
    
    filtros = {
        "nombre": (request.GET.get('nombre') or "").strip()
    }

    categorias_qs = Categoria.objects.all().order_by('nombre')

    if filtros["nombre"]:
        categorias_qs = categorias_qs.filter(nombre__icontains=filtros["nombre"])

    contexto = {
        "categorias": categorias_qs,
        "filtros": filtros,
        "hay_filtro": bool(filtros["nombre"]),
        "total_filtrado": categorias_qs.count(),
        "total_general": Categoria.objects.count(),
        "request": request, 
    }

    return render(request, 'categorias.html', contexto)
