from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import UnidadMedida
from .forms import UnidadForm
from django.urls import reverse_lazy

class UnidadListView(ListView):
    model = UnidadMedida
    template_name = 'unidad/unidad_list.html'  # Crea un archivo HTML para listar las marcas

class UnidadCreateView(CreateView):
    model = UnidadMedida
    form_class = UnidadForm
    template_name = 'unidad/unidad_form.html'  # Crea un archivo HTML para el formulario de creación
    success_url = reverse_lazy('unidad_list')  # Redirige a la lista de marcas después de crear una marca

class UnidadUpdateView(UpdateView):
    model = UnidadMedida
    form_class = UnidadForm
    template_name = 'unidad/unidad_form.html'  # Crea un archivo HTML para el formulario de actualización
    success_url = reverse_lazy('unidad_list')  # Redirige a la lista de marcas después de actualizar una marca

class UnidadDeleteView(DeleteView):
    model = UnidadMedida
    template_name = 'unidad/unidad_confirm_delete.html'  # Crea un archivo HTML para confirmar la eliminación
    success_url = reverse_lazy('unidad_list')  # Redirige a la lista de marcas después de eliminar una marca
