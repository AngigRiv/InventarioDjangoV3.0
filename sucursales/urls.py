from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', SucursalListView.as_view(), name='sucursal_list'),
    path('crear/', SucursalCreateView.as_view(), name='sucursal_create'),
    path('<uuid:pk>/editar/', SucursalUpdateView.as_view(), name='sucursal_update'),
    path('<uuid:pk>/eliminar/', SucursalDeleteView.as_view(), name='sucursal_delete'),


    
]
