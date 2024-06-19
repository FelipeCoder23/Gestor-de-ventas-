from django.shortcuts import render, redirect, get_object_or_404
from .models import Egreso, ProductosEgreso
from .forms import AddItemCarroForm
from django.contrib import messages

def listar_egresos(request):
    egresos = Egreso.objects.all()
    context = {'egresos': egresos}
    return render(request, 'listar_egresos.html', context)

def detalle_egreso(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    items = ProductosEgreso.objects.filter(egreso=egreso)
    form = AddItemCarroForm()
    context = {'egreso': egreso, 'items': items, 'form': form}
    return render(request, 'detalle_egreso.html', context)

def agregar_item_egreso(request, egreso_id):
    if request.method == 'POST':
        egreso = get_object_or_404(Egreso, id=egreso_id)
        form = AddItemCarroForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.egreso = egreso
            item.save()
            messages.success(request, "Producto agregado al carro exitosamente")
        else:
            messages.error(request, "Error al agregar el producto al carro")
    return redirect('detalle_egreso', egreso_id=egreso_id)

def eliminar_item_carro(request, item_id):
    item = get_object_or_404(ProductosEgreso, id=item_id)
    egreso_id = item.egreso.id
    item.delete()
    messages.success(request, "Producto eliminado del carro exitosamente")
    return redirect('detalle_egreso', egreso_id=egreso_id)
