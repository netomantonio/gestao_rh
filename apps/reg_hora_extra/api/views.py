from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from apps.reg_hora_extra.api.serializers import HoraExtraSerializer
from apps.reg_hora_extra.models import HoraExtra


class HoraExtraViewSet(viewsets.ModelViewSet):
    queryset = HoraExtra.objects.all()
    serializer_class = HoraExtraSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

