import io

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from reportlab.pdfgen import canvas

from apps.funcionarios.models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos', ]

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.lower().split(' ')[0] + funcionario.nome.lower().split(' ')[1]
        funcionario.user = User.objects.create(
            username=username)
        funcionario.empresa = self.request.user.funcionario.empresa
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


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(225, 810, 'Relatório de Funcionários')
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)
    str_ = 'Nome: %s | Horas Extras: %.2f'
    p.drawString(113, 800, '_____________________________________________________')
    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extras))
        y -= 20
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):

        params = {
            'today': 'Var today',
            'sales': 'Var sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'mylife')

