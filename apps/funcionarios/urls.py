from django.urls import path

from apps.funcionarios.views import FuncionarioCreate, FuncionarioList, FuncionarioEdit, FuncionarioDelete

urlpatterns = [
    path('novo', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('<int:pk>/editar', FuncionarioEdit.as_view(), name='edit_funcionario'),
    path('<int:pk>/deletar', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('', FuncionarioList.as_view(), name='list_funcionario'),
]