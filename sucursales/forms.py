from django import forms
from inventario.models import Sucursal, Empresa

class SucursalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 
                                   'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)
        # Personalizamos la representación de las opciones del campo empresa
        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"

    class Meta:
        model = Sucursal
        fields = ['empresa', 'nombre_comercial', 'direccion']
        widgets = {
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
