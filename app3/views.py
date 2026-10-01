from django.shortcuts import render


def inicio(request):
    return render(request, 'app3/inicio.html')
