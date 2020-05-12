from django.urls import path

from apps.reg_hora_extra.views import HoraExtraCreate, HoraExtraList, HoraExtraEdit, HoraExtraDelete, \
    HoraExtraEditByFuncionario, UtilizouHoraExtra, NaoUtilizouHoraExtra, CsvExport, ExcelExport

urlpatterns = [
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('<int:pk>/editar', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('editar/<int:pk>', HoraExtraEditByFuncionario.as_view(), name='edit_hora_extra_by_funcionario'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('<int:pk>/deletar', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('csv-export', CsvExport.as_view(), name='csv_export'),
    path('excel-export', ExcelExport.as_view(), name='excel_export'),
]