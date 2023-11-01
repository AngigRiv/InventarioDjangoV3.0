from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Sucursal
from .forms import SucursalForm

# Vista para listar las sucursales
class SucursalListView(ListView):
    model = Sucursal
    template_name = 'sucursal/sucursal_list.html'
    context_object_name = 'sucursales'

    def get_queryset(self):
        # Modificamos la consulta para incluir la razón social de la empresa
        return Sucursal.objects.select_related('empresa')

# Vista para crear una nueva sucursal
class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'sucursal/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')

# Vista para editar una sucursal existente
class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'sucursal/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')

# Vista para eliminar una sucursal
class SucursalDeleteView(DeleteView):
    model = Sucursal
    template_name = 'sucursal/sucursal_confirm_delete.html'
    success_url = reverse_lazy('sucursal_list')