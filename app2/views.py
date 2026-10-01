from django.shortcuts import render


def inicio(request):

    categorias = [
        {
            'id': 1,
            'nombre': 'Computadores',
            'descripcion': 'Notebooks y computadores de escritorio.'
        },
        {
            'id': 2,
            'nombre': 'Periféricos',
            'descripcion': 'Mouse, teclados y accesorios.'
        },
        {
            'id': 3,
            'nombre': 'Monitores',
            'descripcion': 'Pantallas para trabajo y entretenimiento.'
        },
        {
            'id': 4,
            'nombre': 'Accesorios',
            'descripcion': 'Productos complementarios para computadores.'
        }
    ]

    contexto = {
        'categorias': categorias
    }

    return render(request, 'app2/inicio.html', contexto)
