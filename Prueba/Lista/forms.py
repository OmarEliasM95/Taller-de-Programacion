from .models import *
from django.forms import ModelForm
class formulario_producto(ModelForm):
    class Meta:
        model= producto
        fields= '__all__'