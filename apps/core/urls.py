from django.urls import path, include

from apps.core.views import home, celery

urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery'),
]