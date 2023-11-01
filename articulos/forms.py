from django import forms
from inventario.models import *

class ArticuloForm(forms.ModelForm):
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    grupo = forms.ModelChoiceField(queryset=GrupoProveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    linea = forms.ModelChoiceField(queryset=LineaArticulo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sublinea = forms.ModelChoiceField(queryset=SublineaArticulo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    marca = forms.ModelChoiceField(queryset=Marca.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Articulo
        fields = ['codigo_sku', 'descripcion', 'unidad_medida', 'grupo', 'linea', 'sublinea',
                  'empresa', 'factor_compra', 'factor_reparto', 'marca']
        widgets = {
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'factor_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'factor_reparto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        
        self.fields['unidad_medida'].label_from_instance = lambda obj: f"{obj.unidad_nombre}"
        self.fields['grupo'].label_from_instance = lambda obj: f"{obj.codigo_grupo}"
        self.fields['linea'].label_from_instance = lambda obj: f"{obj.codigo_linea}"
        self.fields['sublinea'].label_from_instance = lambda obj: f"{obj.codigo_sublinea}"
        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"
        self.fields['marca'].label_from_instance = lambda obj: f"{obj.marca_nombre}"
