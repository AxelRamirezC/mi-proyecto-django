# principal/views.py
from django.shortcuts import render

def inicio(request):
    context = {
        'titulo': 'Bienvenido a mi proyecto Django',
        'subtitulo': 'Este es el inicio de tu aplicación web'
    }
    return render(request, 'inicio.html', context)

def acerca(request):
    context = {
        'titulo': 'Acerca de',
        'nombre': 'Axel Hadit Ramirez Coronel',
        'proposito': 'Este proyecto tiene como objetivo demostrar las capacidades de Django para crear aplicaciones web completas y funcionales.',
        'tecnologias': ['Django', 'Python', 'Tailwind CSS', 'HTML5']
    }
    return render(request, 'acerca.html', context)