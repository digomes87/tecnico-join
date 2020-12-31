from django.shortcuts import render
from .models import Pessoa

def index(request):
    p = Pessoa.objects.all()
    return render(request, 'pessoas/index.html', {'p':p})


