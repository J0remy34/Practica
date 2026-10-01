from django.shortcuts import render


def inicio(request):

    proveedores = [
        {
            'id': 1,
            'empresa': 'Tech Chile',
            'contacto': 'Carlos Pérez',
            'telefono': '+56 9 1234 5678'
        },
        {
            'id': 2,
            'empresa': 'Digital Store',
            'contacto': 'María González',
            'telefono': '+56 9 2345 6789'
        },
        {
            'id': 3,
            'empresa': 'CompuMarket',
            'contacto': 'Juan Rodríguez',
            'telefono': '+56 9 3456 7890'
        }
    ]

    contexto = {
        'proveedores': proveedores
    }

    return render(request, 'app3/inicio.html', contexto)
