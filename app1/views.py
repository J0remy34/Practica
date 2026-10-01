from django.shortcuts import render


def inicio(request):

    productos = [
        {
            'id': 1,
            'nombre': 'Notebook Lenovo',
            'precio': 599990,
            'stock': 10
        },
        {
            'id': 2,
            'nombre': 'Mouse Logitech',
            'precio': 24990,
            'stock': 25
        },
        {
            'id': 3,
            'nombre': 'Teclado Mecánico',
            'precio': 45990,
            'stock': 15
        },
        {
            'id': 4,
            'nombre': 'Monitor Samsung',
            'precio': 189990,
            'stock': 8
        }
    ]

    contexto = {
        'productos': productos
    }

    return render(request, 'app1/inicio.html', contexto)