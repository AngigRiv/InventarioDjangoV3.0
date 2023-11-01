from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Empresa
from .forms import EmpresaForm
from django.urls import reverse_lazy

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'  # Crea un archivo HTML para listar las marcas

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'  # Crea un archivo HTML para el formulario de creación
    success_url = reverse_lazy('empresa_list')  # Redirige a la lista de marcas después de crear una marca

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'  # Crea un archivo HTML para el formulario de actualización
    success_url = reverse_lazy('empresa_list')  # Redirige a la lista de marcas después de actualizar una marca

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresa/empresa_confirm_delete.html'  # Crea un archivo HTML para confirmar la eliminación
    success_url = reverse_lazy('empresa_list')  # Redirige a la lista de marcas después de eliminar una marca
 