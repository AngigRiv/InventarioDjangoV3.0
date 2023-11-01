from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(views.ItemsListView.as_view()), name='item_list'),
    path('crear/', login_required(views.ItemsCreateView.as_view()), name='item_create'),
    path('<uuid:pk>/editar/', login_required(views.ItemsUpdateView.as_view()), name='item_update'),
    path('<uuid:pk>/eliminar/', login_required(views.ItemsDeleteView.as_view()), name='item_delete'),
]