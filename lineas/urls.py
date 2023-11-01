from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.LineaArticuloListView.as_view(), name='linea_list'),
    path('crear/', views.LineaArticuloCreateView.as_view(), name='linea_create'),
    path('<uuid:pk>/editar/', views.LineaArticuloUpdateView.as_view(), name='linea_update'),
    path('<uuid:pk>/eliminar/', views.LineaArticuloDeleteView.as_view(), name='linea_delete'),
]