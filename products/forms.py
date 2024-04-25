from django import forms
from .models import Producto


    
class AddProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ( "nombre", "descripcion", "precio_compra", "precio_venta", "proveedor", "en_stock")
        labels = {
            
            "nombre": "Nombre producto",
            "descripcion": "Descripción",
            "precio_compra": "Costo producto",
            "precio_venta": "Precio de venta",
            "proveedor": "Proveedor",
            "en_stock": "Cantidad en stock",
        }


class Editarinventarioform(forms.ModelForm):
  

    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "precio_compra", "precio_venta", "proveedor", "en_stock")
        labels = {
            "nombre": "Nombre producto",
            "descripcion": "Descripción",
            "precio_compra": "Costo producto",
            "precio_venta": "Precio de venta",
            "proveedor": "Proveedor",  
            "en_stock": "Cantidad en stock",
            }
        widgets = {
            "nombre": forms.TextInput(attrs={"id": "nombre_editar"}),
            "descripcion": forms.Textarea(attrs={"id": "descripcion_editar", "rows": 3}),
            "precio_compra": forms.NumberInput(attrs={"id": "costo_editar"}),
            "precio_venta": forms.NumberInput(attrs={"id": "precio_venta_editar"}),
            "proveedor": forms.TextInput(attrs={"id": "proveedor_editar"}),
            "en_stock": forms.NumberInput(attrs={"id": "cantidad_editar"}),
        }



class Editarinventarioform2(forms.ModelForm):


    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "precio_compra", "precio_venta", "proveedor", "en_stock")
        labels = {
            "nombre": "Nombre producto",
            "descripcion": "Descripción",
            "precio_compra": "Costo producto",
            "precio_venta": "Precio de venta",
            "proveedor": "Proveedor",
            "en_stock": "Cantidad en stock",
        }
       


class SimpleProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_compra', 'precio_venta', 'proveedor', 'en_stock']
