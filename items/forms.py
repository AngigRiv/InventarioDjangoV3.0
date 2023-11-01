from django import forms
from inventario.models import *

class ItemsForm(forms.ModelForm):
    inventario = forms.ModelChoiceField(
        queryset=Inventario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
    class Meta:
        model = ItemInventario
        fields = ['inventario', 'nro_item', 'articulo', 'stock_fisico', 'devoluciones_pendientes', 'total_unidades_stock', 'precio_costo', 'total_item', 'responsable_linea']
        widgets = {
            'nro_item': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_fisico': forms.NumberInput(attrs={'class': 'form-control'}),
            'devoluciones_pendientes': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_unidades_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_unidades_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_item': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemsForm, self).__init__(*args, **kwargs)

        # Personalizamos la representación de las opciones del campo inventario
        self.fields['inventario'].label_from_instance = lambda obj: f"{obj.fecha_inventario}"

        # Personalizamos la representación de las opciones del campo articulo
        self.fields['articulo'].label_from_instance = lambda obj: f"{obj.codigo_sku}"
