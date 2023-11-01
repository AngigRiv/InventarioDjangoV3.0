from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(EmpresaListView.as_view()), name='empresa_list'),
    path('crear/', login_required(EmpresaCreateView.as_view()), name='empresa_create'),
    path('<uuid:pk>/editar/', login_required(EmpresaUpdateView.as_view()), name='empresa_update'),
    path('<uuid:pk>/eliminar/', login_required(EmpresaDeleteView.as_view()), name='empresa_delete'),
]
