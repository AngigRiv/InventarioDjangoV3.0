from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.GrupoProveedorListView.as_view(), name='grupo_list'),
    path('crear/', views.GrupoProveedorCreateView.as_view(), name='grupo_create'),
    path('<uuid:pk>/editar/', views.GrupoProveedorUpdateView.as_view(), name='grupo_update'),
    path('<uuid:pk>/eliminar/', views.GrupoProveedorDeleteView.as_view(), name='grupo_delete'),
]