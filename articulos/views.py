from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Articulo
from .forms import ArticuloForm

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulo/articulo_list.html'  # Plantilla para listar los artículos
    context_object_name = 'articulos'

    def get_queryset(self):
        # Seleccionar todas las relaciones necesarias en una sola consulta
        return Articulo.objects.select_related('unidad_medida', 'grupo', 'linea', 'sublinea', 'empresa', 'marca')

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'  # Plantilla para el formulario de creación de artículos
    success_url = reverse_lazy('articulo_list')  # Redirige a la lista de artículos después de crear uno

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'   # Plantilla para el formulario de actualización de artículos
    success_url = reverse_lazy('articulo_list')  # Redirige a la lista de artículos después de actualizar uno

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulo/articulo_confirm_delete.html' # Plantilla para confirmar la eliminación de artículos
    success_url = reverse_lazy('articulo_list')
