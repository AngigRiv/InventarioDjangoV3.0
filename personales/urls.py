from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', PersonalListView.as_view(), name='personal_list'),
    path('crear/', PersonalCreateView.as_view(), name='personal_create'),
    path('<uuid:pk>/editar/', PersonalUpdateView.as_view(), name='personal_update'),
    path('<uuid:pk>/eliminar/', PersonalDeleteView.as_view(), name='personal_delete'),
]
