from django.db import models
from prova.cargos.models import Cargos


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CharField)
    admissao = models.DateTimeField('Data de Admissão')

    class Meta:
        ordering = ["admissao"]

    def __str__(self):
        return self.nome
