from django import forms
from inventario.models import SublineaArticulo, LineaArticulo

class SublineaArticuloForm(forms.ModelForm):
    linea = forms.ModelChoiceField(queryset=LineaArticulo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SublineaArticulo
        fields = ['codigo_sublinea', 'sublinea_descripcion', 'linea', 'estado']
        widgets = {
            'codigo_sublinea': forms.TextInput(attrs={'class': 'form-control'}),
            'sublinea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(SublineaArticuloForm, self).__init__(*args, **kwargs)
        
        # Personalizamos la representación de las opciones del campo linea
        self.fields['linea'].label_from_instance = lambda obj: f"{obj.codigo_linea}"