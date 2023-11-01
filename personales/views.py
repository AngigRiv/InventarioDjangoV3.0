from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventario.models import Personal
from .forms import PersonalForm

class PersonalListView(ListView):
    model = Personal
    template_name = 'personal/personal_list.html'
    context_object_name = 'personales'

    def get_queryset(self):
        # Modificamos la consulta para incluir la razón social de la empresa
        return Personal.objects.select_related('empresa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_documento_choices'] = PersonalForm.TIPO_DOCUMENTO_CHOICES
        return context

# Vista para crear un nueva personal
class PersonalCreateView(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/personal_form.html'
    success_url = reverse_lazy('personal_list')

class PersonalUpdateView(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/personal_form.html'  # Corrige esta línea
    success_url = reverse_lazy('personal_list')

# Vista para eliminar unn personal
class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = 'personal/personal_confirm_delete.html'
    success_url = reverse_lazy('personal_list')