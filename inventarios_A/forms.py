import datetime
import re
from django import forms
from inventario.models import Inventario, Sucursal, Empresa, Personal
from django.shortcuts import render
from django.contrib.auth import get_user_model  # Importa el modelo de usuario


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'date'
        
class InventarioForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sucursal = forms.ModelChoiceField(
        queryset=Sucursal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    hora_inicio = forms.ChoiceField(
        choices=[(f"{i:02d}:{j:02d}", f"{i:02d}:{j:02d}") for i in range(24) for j in range(0, 60, 15)],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    hora_fin = forms.ChoiceField(
        choices=[(f"{i:02d}:{j:02d}", f"{i:02d}:{j:02d}") for i in range(24) for j in range(0, 60, 15)],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    creado_por = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    cerrado_por = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super(InventarioForm, self).__init__(*args, **kwargs)
        # Personalizamos la representación de las opciones del campo empresa y sucursal
        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"
        self.fields['sucursal'].label_from_instance = lambda obj: f"{obj.nombre_comercial}"
        self.fields['personal'].label_from_instance = lambda obj: f"{obj.nombre_personal}"
        
    def clean(self):
        cleaned_data = super().clean()
        fecha_inventario = cleaned_data.get('fecha_inventario')
        empresa = cleaned_data.get('empresa')
        sucursal = cleaned_data.get('sucursal')

        if fecha_inventario and empresa and sucursal:
            same_inventarios = Inventario.objects.filter(
                fecha_inventario=fecha_inventario,
                empresa=empresa,
                sucursal=sucursal
            )

            if self.instance:  # Excluye el propio inventario actual al actualizar
                same_inventarios = same_inventarios.exclude(pk=self.instance.pk)

            if same_inventarios.exists():
                self.add_error(
                    'fecha_inventario',
                    'Ya existe un inventario para esta fecha, empresa y sucursal.'
                )
       
    def crear_inventario(request):
           if request.method == 'POST':
            form = InventarioForm(request.POST)
           if form.is_valid():
            # Procesa el formulario y guarda el objeto Inventario si es válido
            inventario = form.save()
            # Puedes realizar otras acciones, como redireccionar a la página de detalles del inventario
           else:
             form = InventarioForm()  # Crea una instancia del formulario en el método GET

             return render(request, 'tu_template.html', {'form': form})


    class Meta:
        model = Inventario
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario
        fields = ['empresa', 'sucursal', 'fecha_inventario', 'nro_inventario',
                  'personal', 'hora_inicio', 'hora_fin', 'total_inventario',
                  'estado', 'creado_por','cerrado_por']
        widgets = {
            'fecha_inventario': DateTimeInput(attrs={'class': 'form-control'}),
            'nro_inventario': forms.TextInput(attrs={'class': 'form-control'}),
            #'personal': forms.TextInput(attrs={'class': 'form-control'}),
            #'hora_inicio': forms.TimeInput(attrs={'class': 'form-control '}),
            'total_inventario': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'custom-select'}),
            #'creado_por': forms.TextInput(attrs={'class': 'form-control'}),
            #'cerrado_por': forms.TextInput(attrs={'class': 'form-control'}),

        }
