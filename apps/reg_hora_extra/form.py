from django.forms import ModelForm

from apps.funcionarios.models import Funcionario
from apps.reg_hora_extra.models import HoraExtra


class HoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(HoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = HoraExtra
        fields = ['motivo', 'funcionario', 'horas']
