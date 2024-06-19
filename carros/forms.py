from django import forms
from .models import ProductosEgreso

class AddItemCarroForm(forms.ModelForm):
    class Meta:
        model = ProductosEgreso
        fields = ['producto', 'cantidad']
