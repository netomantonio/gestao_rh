from django.conf import settings
# from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.reg_hora_extra.api.views import HoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/horas-extras', HoraExtraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.reg_hora_extra.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

