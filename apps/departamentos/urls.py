from django.urls import path

from apps.departamentos.views import DepartamentoCreate, DepartamentoList, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('<int:pk>/editar', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('<int:pk>/deletar', DepartamentoDelete.as_view(), name='delete_departamento'),
    path('', DepartamentoList.as_view(), name='list_departamento'),
]