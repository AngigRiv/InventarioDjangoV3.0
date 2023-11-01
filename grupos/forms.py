from django import forms
from inventario.models import Empresa, Personal, GrupoProveedor

class GrupoProveedorForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    responsable_grupo = forms.ModelChoiceField(queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = GrupoProveedor
        fields = ['codigo_grupo', 'grupo_descripcion', 'empresa', 'activo', 'responsable_grupo']
        widgets = {
            'codigo_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(GrupoProveedorForm, self).__init__(*args, **kwargs)
        
        # Personalizamos la representación de las opciones del campo empresa
        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"

        # Personalizamos la representación de las opciones del campo responsable_grupo
        self.fields['responsable_grupo'].label_from_instance = lambda obj: f"{obj.nombre_personal}"
