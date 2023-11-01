from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import GrupoProveedor
from .forms import GrupoProveedorForm

class GrupoProveedorListView(ListView):
    model = GrupoProveedor
    template_name = 'grupo/grupo_list.html'  # Crea un archivo HTML para listar los grupos proveedor
    context_object_name = 'grupos'

    def get_queryset(self):
        # Modificamos la consulta para incluir la razón social de la empresa
        return GrupoProveedor.objects.select_related('empresa')
    
    def get_queryset(self):
        # Modificamos la consulta para incluir nombre del personal
        return GrupoProveedor.objects.select_related('responsable_grupo')

class GrupoProveedorCreateView(CreateView):
    model = GrupoProveedor
    form_class = GrupoProveedorForm
    template_name = 'grupo/grupo_form.html'  # Crea un archivo HTML para el formulario de creación
    success_url = reverse_lazy('grupo_list')  # Redirige a la lista de grupos proveedor después de crear uno

class GrupoProveedorUpdateView(UpdateView):
    model = GrupoProveedor
    form_class = GrupoProveedorForm
    template_name = 'grupo/grupo_form.html'   # Crea un archivo HTML para el formulario de actualización
    success_url = reverse_lazy('grupo_list')  # Redirige a la lista de grupos proveedor después de actualizar uno

class GrupoProveedorDeleteView(DeleteView):
    model = GrupoProveedor
    template_name = 'grupo/grupo_confirm_delete.html' # Crea un archivo HTML para confirmar la eliminación
    success_url = reverse_lazy('grupo_list')
