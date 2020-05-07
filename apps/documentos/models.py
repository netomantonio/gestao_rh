from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario
from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario

def user_directory_path(instance,filename):
    namefile = instance.descricao
    extensao = filename.split('.')
    return 'documentos/funcionario_{0}/{1}.{2}'.format(instance.funcionario.id, namefile, extensao[1])


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to=user_directory_path)

    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.funcionario.id])


    def __str__(self):
        return self.descricao

