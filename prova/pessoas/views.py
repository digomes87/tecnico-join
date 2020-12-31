from django.shortcuts import render
from .models import Pessoa, Mapa
from .forms import MapaForm
from django.urls import reverse_lazy
from django import forms


def index(request):
    p = Pessoa.objects.all()
    form = MapaForm()

    if request.method == 'POST':
        form =  MapaForm(request.POST)
        if form.is_valid(): 
            form.save()
            form = MapaForm()
        else:
            form = MapaForm()

    return render(request, 'pessoas/index.html', {'p':p, 'form':form})    
