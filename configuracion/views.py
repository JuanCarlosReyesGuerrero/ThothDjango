from django.shortcuts import render


# Create your views here.
from configuracion.models import Idioma, Municipio


def myfirstview(request):
    data = {
        'name': 'juan',
        'idiomas': Idioma.objects.all()
    }
    return render(request, 'home.html', data)

def mysecondview(request):
    data = {
        'name': 'juan',
        'idiomas': Idioma.objects.all(),
        'municipios': Municipio.objects.all()
    }
    return render(request, 'second.html', data)
