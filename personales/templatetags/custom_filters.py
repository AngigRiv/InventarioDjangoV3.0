from django import template
from personales.forms import PersonalForm  # Asegúrate de importar PersonalForm desde tu aplicación

register = template.Library()

@register.filter
def get_tipo_documento(value):
    # Convierte el valor numérico en la descripción correspondiente
    choices = dict(PersonalForm.TIPO_DOCUMENTO_CHOICES)
    return choices.get(value, value)
