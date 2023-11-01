from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', UnidadListView.as_view(), name='unidad_list'),
    path('crear/', UnidadCreateView.as_view(), name='unidad_create'),
    path('<uuid:pk>/editar/', UnidadUpdateView.as_view(), name='unidad_update'),
    path('<uuid:pk>/eliminar/', UnidadDeleteView.as_view(), name='unidad_delete'),
]
