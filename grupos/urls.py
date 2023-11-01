from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(views.GrupoProveedorListView.as_view()), name='grupo_list'),
    path('crear/', login_required(views.GrupoProveedorCreateView.as_view()), name='grupo_create'),
    path('<uuid:pk>/editar/', login_required(views.GrupoProveedorUpdateView.as_view()), name='grupo_update'),
    path('<uuid:pk>/eliminar/', login_required(views.GrupoProveedorDeleteView.as_view()), name='grupo_delete'),
]