from django.shortcuts import render

def inicio(request):
    context = {
        'titulo': 'Bienvenido a mi proyecto Django',
        'subtitulo': 'Este es tu primer template en Django 🎉'
    }
    return render(request, 'inicio.html', context)

def acerca(request):
    context = {
        'titulo': 'Acerca de',
        'nombre': 'Angel Fabian Vázquez Ramirez',
        'proposito': 'Este proyecto nos enseña las capacidades de Django para crear aplicaciones web completas, seguras y funcionales.',
    }
    return render(request, 'acerca.html', context)