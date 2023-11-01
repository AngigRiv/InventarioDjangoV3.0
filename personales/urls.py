from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(PersonalListView.as_view()), name='personal_list'),
    path('crear/', login_required(PersonalCreateView.as_view()), name='personal_create'),
    path('<uuid:pk>/editar/', login_required(PersonalUpdateView.as_view()), name='personal_update'),
    path('<uuid:pk>/eliminar/', login_required(PersonalDeleteView.as_view()), name='personal_delete'),
]
