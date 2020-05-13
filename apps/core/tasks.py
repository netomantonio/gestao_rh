from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

from apps.funcionarios.models import Funcionario


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_funcionarios():
    return Funcionario.objects.count()


@shared_task
def rename_funcionario(funcionario_id, name):
    w = Funcionario.objects.get(id=funcionario_id)
    w.nome = name
    w.save()

@shared_task
def send_relatorio():
    total = Funcionario.objects.count()
    send_mail(
        'Relatório Celery',
        'Relatório geral de funcionarios %f' % total,
        'makllaus@gmail.com',
        ['antoniomnjobs@gmail.com'],
        fail_silently=False,
    )
    return True