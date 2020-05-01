from django.urls import path, include

from apps.empresas.views import EmpresaCreate,EmpresaEdit

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('<int:pk>/editar', EmpresaEdit.as_view(), name='edit_empresa'),
]