from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(MarcaListView.as_view()), name='marca_list'),
    path('crear/', login_required(MarcaCreateView.as_view()), name='marca_create'),
    path('<uuid:pk>/editar/', login_required(MarcaUpdateView.as_view()), name='marca_update'),
    path('<uuid:pk>/eliminar/', login_required(MarcaDeleteView.as_view()), name='marca_delete'),
]
