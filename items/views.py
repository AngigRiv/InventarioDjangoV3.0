from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import ItemInventario
from .forms import ItemsForm

class ItemsListView(ListView):
    model = ItemInventario
    template_name = 'item/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        # Seleccionar todas las relaciones necesarias en una sola consulta
        return ItemInventario.objects.select_related('inventario', 'articulo')
    
class ItemsCreateView(CreateView):
    model = ItemInventario
    form_class = ItemsForm
    template_name = 'item/item_form.html'
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        # Verificar nuevamente la unicidad de artículo en el inventario antes de guardar
        inventario = form.cleaned_data.get('inventario')
        articulo = form.cleaned_data.get('articulo')

        if ItemInventario.objects.filter(inventario=inventario, articulo=articulo).exists():
            form.add_error(None, "Este artículo ya existe en el inventario.")
            return self.form_invalid(form)

        return super().form_valid(form)

class ItemsUpdateView(UpdateView):
    model = ItemInventario
    form_class = ItemsForm
    template_name = 'item/item_form.html' 
    success_url = reverse_lazy('item_list')

class ItemsDeleteView(DeleteView):
    model = ItemInventario
    template_name = 'item/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
