from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.documentos.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.request.user.pk
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('edit_funcionario', args=[self.request.user.pk])

class DocumentoList(ListView):
    model = Documento


class DocumentoEdit(UpdateView):
    model = Documento
    fields = ['descricao','arquivo']


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documento')