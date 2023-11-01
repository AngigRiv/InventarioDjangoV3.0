from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.SublineaArticuloListView.as_view(), name='sublinea_list'),
    path('crear/', views.SublineaArticuloCreateView.as_view(), name='sublinea_create'),
    path('<uuid:pk>/editar/', views.SublineaArticuloUpdateView.as_view(), name='sublinea_update'),
    path('<uuid:pk>/eliminar/', views.SublineaArticuloDeleteView.as_view(), name='sublinea_delete'),
]