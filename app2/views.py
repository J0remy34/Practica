from django.shortcuts import render


def inicio(request):

    lista_elementos = [
        {
            'id': 1,
            'nombre': 'Elemento 1'
        },
        {
            'id': 2,
            'nombre': 'Elemento 2'
        },
        {
            'id': 3,
            'nombre': 'Elemento 3'
        },
        {
            'id': 4,
            'nombre': 'Elemento 4'
        }
    ]

    contexto = {
        'lista_elementos': lista_elementos
    }

    return render(request, 'app2/inicio.html', contexto)
