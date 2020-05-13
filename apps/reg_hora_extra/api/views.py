from rest_framework import viewsets, permissions

from apps.reg_hora_extra.api.serializers import HoraExtraSerializer
from apps.reg_hora_extra.models import HoraExtra


class HoraExtraViewSet(viewsets.ModelViewSet):
    queryset = HoraExtra.objects.all()
    serializer_class = HoraExtraSerializer
    permission_classes = [permissions.IsAuthenticated]

