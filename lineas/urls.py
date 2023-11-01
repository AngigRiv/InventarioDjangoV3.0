from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(views.LineaArticuloListView.as_view()), name='linea_list'),
    path('crear/', login_required(views.LineaArticuloCreateView.as_view()), name='linea_create'),
    path('<uuid:pk>/editar/', login_required(views.LineaArticuloUpdateView.as_view()), name='linea_update'),
    path('<uuid:pk>/eliminar/', login_required(views.LineaArticuloDeleteView.as_view()), name='linea_delete'),
]