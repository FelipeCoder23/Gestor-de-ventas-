from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Venta
from carros.models import Egreso, ProductosEgreso

def listar_carros(request):
    carros_usados = Egreso.objects.filter(usado=True)
    carros_no_usados = Egreso.objects.filter(usado=False)
    return render(request, 'listar_carros.html', {'carros_usados': carros_usados, 'carros_no_usados': carros_no_usados})

def realizar_venta(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    if request.method == 'POST':
        metodo_pago = request.POST['metodo_pago']
        total = sum(item.subtotal for item in ProductosEgreso.objects.filter(egreso=egreso))
        venta = Venta.objects.create(egreso=egreso, metodo_pago=metodo_pago, total=total)
        egreso.usado = False
        egreso.save()
        messages.success(request, "Venta realizada exitosamente")
        return redirect('listar_carros')
    return render(request, 'realizar_venta.html', {'egreso': egreso})

def ventas_diarias(request):
    hoy = timezone.now().date()
    ventas = Venta.objects.filter(fecha_venta__date=hoy)
    total_vendido = sum(venta.total for venta in ventas)
    return render(request, 'ventas_diarias.html', {'ventas': ventas, 'total_vendido': total_vendido})
