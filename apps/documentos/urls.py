from django.urls import path

from apps.documentos.models import Documento
from apps.documentos.views import DocumentoCreate, DocumentoList, DocumentoEdit, DocumentoDelete

urlpatterns = [
    path('novo/<int:pk>', DocumentoCreate.as_view(), name='create_documento'),
    path('<int:pk>/editar', DocumentoEdit.as_view(), name='edit_documento'),
    path('<int:pk>/deletar', DocumentoDelete.as_view(), name='delete_documento'),
    path('', DocumentoList.as_view(), name='list_documento'),
]