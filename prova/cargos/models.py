from django.db import models


class Cargos(models.Model):
    cargo = models.CharField(max_length=300)


    def __str__(self):
        return self.cargo
