from django.db import models

# Create your models here.from django.db import models


class Producto(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    proveedor = models.CharField(max_length=200)

    en_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
