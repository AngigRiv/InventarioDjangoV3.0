from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ArticuloListView.as_view(), name='articulo_list'),
    path('crear/', views. ArticuloCreateView.as_view(), name='articulo_create'),
    path('<uuid:pk>/editar/', views.ArticuloUpdateView.as_view(), name='articulo_update'),
    path('<uuid:pk>/eliminar/', views.ArticuloDeleteView.as_view(), name='articulo_delete'),
]