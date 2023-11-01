from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(UnidadListView.as_view()), name='unidad_list'),
    path('crear/', login_required(UnidadCreateView.as_view()), name='unidad_create'),
    path('<uuid:pk>/editar/', login_required(UnidadUpdateView.as_view()), name='unidad_update'),
    path('<uuid:pk>/eliminar/', login_required(UnidadDeleteView.as_view()), name='unidad_delete'),
]
