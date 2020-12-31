from django.forms import ModelForm
from .models import Mapa

class MapaForm(ModelForm):
    class Meta:
        model = Mapa
        fields = ['identificador', 'nome', 'latitude', 'longitude']