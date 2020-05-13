from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from apps.reg_hora_extra.api.serializers import HoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):

    horaextra_set = HoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'total_horas_extras', 'horaextra_set']
