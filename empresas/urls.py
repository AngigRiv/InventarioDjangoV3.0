from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', EmpresaListView.as_view(), name='empresa_list'),
    path('crear/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('<uuid:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('<uuid:pk>/eliminar/', EmpresaDeleteView.as_view(), name='empresa_delete'),
]
