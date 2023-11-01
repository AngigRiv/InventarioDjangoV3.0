from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Inventario
from .forms import InventarioForm

# Vista para listar las sucursales
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario_a/inventario_a_list.html'
    context_object_name = 'inventarios_A'

    def get_queryset(self):
        # Modificamos la consulta para incluir la razón social de la empresa
        return Inventario.objects.select_related('empresa')

# Vista para crear una nueva sucursal
class InventarioCreateView(CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario_a/inventario_a_form.html'
    success_url = reverse_lazy('inventario_a_list')

# Vista para editar una sucursal existente
class InventarioUpdateView(UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario_a/inventario_a_form.html'
    success_url = reverse_lazy('inventario_a_list')

# Vista para eliminar una sucursal
class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'inventario_a/inventario_a_confirm_delete.html'
    success_url = reverse_lazy('inventario_a_list')