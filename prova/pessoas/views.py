from django.shortcuts import render
from .models import Pessoa

def index(request):
    p = Pessoa.objects.all()
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'pessoas/index.html', {'p':p, 'mapbox_access_token': mapbox_access_token })


def Coordenada(request):
    pass