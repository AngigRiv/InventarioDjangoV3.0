from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventario.models import LineaArticulo
from .forms import LineaArticuloForm

class LineaArticuloListView(ListView):
    model = LineaArticulo
    template_name = 'linea/linea_list.html'
    context_object_name = 'lineas'  # Opcional: Cambia el nombre del objeto en la plantilla

    def get_queryset(self):
        return LineaArticulo.objects.select_related('grupo')
    
    def get_queryset(self):
        # Modificamos la consulta para incluir nombre del personal
        return LineaArticulo.objects.select_related('responsable_linea')

class LineaArticuloCreateView(CreateView):
    model = LineaArticulo
    form_class = LineaArticuloForm
    template_name = 'linea/linea_form.html'
    success_url = reverse_lazy('linea_list')

class LineaArticuloUpdateView(UpdateView):
    model = LineaArticulo
    form_class = LineaArticuloForm
    template_name = 'linea/linea_form.html'
    success_url = reverse_lazy('linea_list')

class LineaArticuloDeleteView(DeleteView):
    model = LineaArticulo
    template_name = 'linea/linea_confirm_delete.html'
    success_url = reverse_lazy('linea_list')
