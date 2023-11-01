from django import forms
from inventario.models import LineaArticulo, GrupoProveedor, Personal

class LineaArticuloForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(queryset=GrupoProveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    responsable_linea= forms.ModelChoiceField(queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = LineaArticulo
        fields = ['codigo_linea', 'linea_descripcion', 'grupo', 'activo', 'responsable_linea']
        widgets = {
            'codigo_linea': forms.TextInput(attrs={'class': 'form-control'}),
            'linea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(LineaArticuloForm, self).__init__(*args, **kwargs)
        
        # Personalizamos la representación de las opciones del campo empresa
        self.fields['grupo'].label_from_instance = lambda obj: f"{obj.codigo_grupo}"

        # Personalizamos la representación de las opciones del campo responsable_grupo
        self.fields['responsable_linea'].label_from_instance = lambda obj: f"{obj.nombre_personal}"
