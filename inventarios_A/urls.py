from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(InventarioListView.as_view()), name='inventario_a_list'),
    path('crear/', login_required(InventarioCreateView.as_view()), name='inventario_a_create'),
    path('<uuid:pk>/editar/', login_required(InventarioUpdateView.as_view()), name='inventario_a_update'),
    path('<uuid:pk>/eliminar/', login_required(InventarioDeleteView.as_view()), name='inventario_a_delete'),


    
]
