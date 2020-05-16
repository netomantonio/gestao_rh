from django.db import models

class Teste(models.Model):
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.descricao

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome
