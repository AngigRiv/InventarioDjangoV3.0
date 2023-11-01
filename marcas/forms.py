from django import forms
from inventario.models import Marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['codigo_marca', 'marca_nombre']
        widgets = {
            'codigo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
    