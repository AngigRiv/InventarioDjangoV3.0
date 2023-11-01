from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', MarcaListView.as_view(), name='marca_list'),
    path('crear/', MarcaCreateView.as_view(), name='marca_create'),
    path('<uuid:pk>/editar/', MarcaUpdateView.as_view(), name='marca_update'),
    path('<uuid:pk>/eliminar/', MarcaDeleteView.as_view(), name='marca_delete'),
]
