from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Marca
from .forms import MarcaForm
from django.urls import reverse_lazy

class MarcaListView(ListView):
    model = Marca
    template_name = 'marca/marca_list.html'  # Crea un archivo HTML para listar las marcas

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/marca_form.html'  # Crea un archivo HTML para el formulario de creación
    success_url = reverse_lazy('marca_list')  # Redirige a la lista de marcas después de crear una marca

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/marca_form.html'  # Crea un archivo HTML para el formulario de actualización
    success_url = reverse_lazy('marca_list')  # Redirige a la lista de marcas después de actualizar una marca

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/marca_confirm_delete.html'  # Crea un archivo HTML para confirmar la eliminación
    success_url = reverse_lazy('marca_list')  # Redirige a la lista de marcas después de eliminar una marca
