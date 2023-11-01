from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(SucursalListView.as_view()), name='sucursal_list'),
    path('crear/', login_required(SucursalCreateView.as_view()), name='sucursal_create'),
    path('<uuid:pk>/editar/', login_required(SucursalUpdateView.as_view()), name='sucursal_update'),
    path('<uuid:pk>/eliminar/', login_required(SucursalDeleteView.as_view()), name='sucursal_delete'),


    
]
