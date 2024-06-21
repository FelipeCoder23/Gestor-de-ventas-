from django.db import models

from carros.models import Egreso, ProductosEgreso

class Venta(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=[('Efectivo', 'Efectivo'), ('Debito', 'Débito'), ('Credito', 'Crédito')])
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - {self.egreso}"
