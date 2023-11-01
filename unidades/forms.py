from django import forms
from inventario.models import UnidadMedida

class UnidadForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['unidad_nombre']
        widgets = {
            'unidad_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
