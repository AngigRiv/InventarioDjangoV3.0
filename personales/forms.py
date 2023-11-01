from django import forms
from empresas import models
from inventario.models import Personal, Empresa

class PersonalForm(forms.ModelForm):
    # Define las opciones de tipo de documento con números como valores
    TIPO_DOCUMENTO_CHOICES = (
        (1, 'DNI'),
        (2, 'Carnet de Extranjeria'),
        (3, 'Otro'),
    )
    
    tipo_documento = forms.ChoiceField(
        choices=TIPO_DOCUMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        # Personaliza la representación de las opciones del campo tipo_documento
        self.fields['tipo_documento'].choices = [(choice[0], choice[1]) for choice in self.TIPO_DOCUMENTO_CHOICES]

        # Personaliza la representación de las opciones del campo empresa
        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"

    class Meta:
        model = Personal
        fields = ['nombre_personal', 'direccion_personal', 'tipo_documento', 'nro_documento', 'empresa']
        widgets = {
            'nombre_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
        }
