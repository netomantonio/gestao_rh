from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome
