from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(views.ArticuloListView.as_view()), name='articulo_list'),
    path('crear/', login_required(views. ArticuloCreateView.as_view()), name='articulo_create'),
    path('<uuid:pk>/editar/',  login_required(views.ArticuloUpdateView.as_view()), name='articulo_update'),
    path('<uuid:pk>/eliminar/',  login_required(views.ArticuloDeleteView.as_view()), name='articulo_delete'),
]