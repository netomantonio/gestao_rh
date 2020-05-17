from django.urls import path, include

from apps.core.views import home, celery, home2

urlpatterns = [
    path('', home, name='home'),
    path('home', home2, name='home2'),
    path('celery/', celery, name='celery'),
]