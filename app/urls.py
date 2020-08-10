from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^obra/listar/', listar_obra, name='listar_obra'),
    url(r'^obra/perfil/(?P<pk>[0-9]+)', perfil_obra, name='perfil_obra'),
]