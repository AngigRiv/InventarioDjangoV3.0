from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', InventarioListView.as_view(), name='inventario_a_list'),
    path('crear/', InventarioCreateView.as_view(), name='inventario_a_create'),
    path('<uuid:pk>/editar/', InventarioUpdateView.as_view(), name='inventario_a_update'),
    path('<uuid:pk>/eliminar/', InventarioDeleteView.as_view(), name='inventario_a_delete'),


    
]
