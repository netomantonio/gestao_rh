from django.urls import path

from apps.reg_hora_extra.views import HoraExtraCreate, HoraExtraList, HoraExtraEdit, HoraExtraDelete

urlpatterns = [
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('<int:pk>/editar', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('<int:pk>/deletar', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
]