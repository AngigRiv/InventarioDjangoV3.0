from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import ItemInventario
from .forms import ItemsForm
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
<<<<<<< HEAD
    template_name = 'item/item_form.html' 
    success_url = reverse_lazy('item_list') 

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def some_view(request):
    # ...
       item_inventario = ItemInventario(some_field=some_value)
       item_inventario.save(request=request)
       
    def form_valid(self, form):
        # Obtén el usuario actual
        user = self.request.user
     # Comprueba si el usuario actual es responsable de la línea
        if not form.instance.is_responsible_for_item(user):
            raise PermissionDenied("No tienes permiso para agregar este artículo al inventario.")

        # Establece el usuario actual en el modelo antes de guardarlo
        form.instance.responsable_linea = user
        return super().form_valid(form)   
    
    
=======
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

>>>>>>> fa078220cb821e58130d7bdeaec719092ea69db6
class ItemsUpdateView(UpdateView):
    model = ItemInventario
    form_class = ItemsForm
    template_name = 'item/item_form.html' 
    success_url = reverse_lazy('item_list')

class ItemsDeleteView(DeleteView):
    model = ItemInventario
    template_name = 'item/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
