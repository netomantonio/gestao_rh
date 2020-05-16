from django.contrib import admin

from apps.app_antiga.models import Teste, Usuarios


# class UsuariosAdmin(admin.ModelAdmin):
#     fields = ['nome', 'idade', 'salario']
#
#     def get_queryset(self, request):
#         return Usuarios.objects.using('antigo').all()


admin.site.register(Teste)
admin.site.register(Usuarios)
