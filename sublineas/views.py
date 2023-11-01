from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventario.models import SublineaArticulo
from .forms import SublineaArticuloForm

class SublineaArticuloListView(ListView):
    model = SublineaArticulo
    template_name = 'sublinea/sublinea_list.html'
    context_object_name = 'sublineas'  # Opcional: Cambia el nombre del objeto en la plantilla

    def get_queryset(self):
        return SublineaArticulo.objects.select_related('linea')

class SublineaArticuloCreateView(CreateView):
    model = SublineaArticulo
    form_class = SublineaArticuloForm
    template_name = 'sublinea/sublinea_form.html'
    success_url = reverse_lazy('sublinea_list')

class SublineaArticuloUpdateView(UpdateView):
    model = SublineaArticulo
    form_class = SublineaArticuloForm
    template_name = 'sublinea/sublinea_form.html'
    success_url = reverse_lazy('sublinea_list')

class SublineaArticuloDeleteView(DeleteView):
    model = SublineaArticulo
    template_name = 'sublinea/sublinea_confirm_delete.html'
    success_url = reverse_lazy('sublinea_list')
