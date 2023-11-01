from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(views.SublineaArticuloListView.as_view()), name='sublinea_list'),
    path('crear/', login_required(views.SublineaArticuloCreateView.as_view()), name='sublinea_create'),
    path('<uuid:pk>/editar/', login_required(views.SublineaArticuloUpdateView.as_view()), name='sublinea_update'),
    path('<uuid:pk>/eliminar/', login_required(views.SublineaArticuloDeleteView.as_view()), name='sublinea_delete'),
]