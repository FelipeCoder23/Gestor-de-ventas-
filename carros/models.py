from django.db import models
from products.models import Producto
from django.forms import model_to_dict

class Egreso(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    numero_carro = models.PositiveIntegerField(unique=True, default=0)
    usado = models.BooleanField(default=False)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'

    def __str__(self):
        return f'Carro {self.numero_carro} - {self.fecha_pedido}'

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'

    def __str__(self):
        return self.producto

    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item
