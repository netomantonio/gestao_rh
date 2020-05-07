from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.funcionarios.models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos',]

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.lower().split(' ')[0] + funcionario.nome.lower().split(' ')[1]
        funcionario.user = User.objects.create(
            username=username)
        funcionario.empresa=self.request.user.funcionario.empresa
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)

class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_funcionario = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_funcionario)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')