import csv
import json

import xlwt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
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


class HoraExtraEditByFuncionario(UpdateView):
    model = HoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    # def get_success_url(self):
    #     return reverse('edit_hora_extra_by_funcionario', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditByFuncionario, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_hora_extra')

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        this_hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        this_hora_extra.utilizada = True
        this_hora_extra.save()

        funcionario = self.request.user.funcionario
        response = json.dumps({'mensagem': 'Requisição executada', 'horas': funcionario.total_horas_extras})
        return HttpResponse(response, content_type='application/json')


class NaoUtilizouHoraExtra(View):

    def post(self, *args, **kwargs):
        this_hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        this_hora_extra.utilizada = False
        this_hora_extra.save()

        funcionario = self.request.user.funcionario
        response = json.dumps({'mensagem': 'Requisição executada', 'horas': funcionario.total_horas_extras})
        return HttpResponse(response, content_type='application/json')


class CsvExport(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bancoDeHoras.csv"'
        banco_horas = HoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'MOTIVO', 'FUNCIONARIO', 'QNT HORAS', 'HORAS RESTANTES'])
        for hora_extra in banco_horas:
            writer.writerow([hora_extra.id, hora_extra.motivo, hora_extra.funcionario, hora_extra.horas, hora_extra.funcionario.total_horas_extras])
        return response

class ExcelExport(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ID', 'MOTIVO', 'FUNCIONARIO', 'HORAS', 'HORAS RESTANTES']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        banco_horas = HoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for hora_extra in banco_horas:
            ws.write(row_num, 0, hora_extra.id)
            ws.write(row_num, 1, hora_extra.motivo)
            ws.write(row_num, 2, hora_extra.funcionario.nome)
            ws.write(row_num, 3, hora_extra.horas)
            ws.write(row_num, 4, hora_extra.funcionario.total_horas_extras)
            row_num += 1
        wb.save(response)
        return response

