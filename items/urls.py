from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ItemsListView.as_view(), name='item_list'),
    path('crear/', views.  ItemsCreateView.as_view(), name='item_create'),
    path('<uuid:pk>/editar/', views. ItemsUpdateView.as_view(), name='item_update'),
    path('<uuid:pk>/eliminar/', views. ItemsDeleteView.as_view(), name='item_delete'),
]