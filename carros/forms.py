from django import forms
from .models import ProductosEgreso, Egreso

class AddItemCarroForm(forms.ModelForm):
    class Meta:
        model = ProductosEgreso
        fields = ['producto', 'cantidad']


class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ['numero_carro']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_carro'].queryset = Egreso.objects.filter(usado=False)
