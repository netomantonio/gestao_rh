from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.reg_hora_extra.form import HoraExtraForm
from apps.reg_hora_extra.models import HoraExtra


class HoraExtraCreate(CreateView):
    model = HoraExtra
    form_class = HoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_funcionario = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_funcionario)

class HoraExtraEdit(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_hora_extra')
