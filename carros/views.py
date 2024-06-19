from django.shortcuts import render, redirect, get_object_or_404
from .models import Egreso, ProductosEgreso
from products.models import Producto
from .forms import AddItemCarroForm, EgresoForm
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

def asignar_carro(request):
    if request.method == 'POST':
        form = EgresoForm(request.POST)
        if form.is_valid():
            egreso = form.save(commit=False)
            egreso.usado = True
            egreso.save()
            return redirect('agregar_productos', egreso_id=egreso.id)
    else:
        form = EgresoForm()
    return render(request, 'asignar_carro.html', {'form': form})

def agregar_productos(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        producto = get_object_or_404(Producto, id=producto_id)
        item, created = ProductosEgreso.objects.get_or_create(egreso=egreso, producto=producto, defaults={'cantidad': cantidad})
        if not created:
            item.cantidad += cantidad
            item.save()
        messages.success(request, "Producto agregado al carro exitosamente")
        return redirect('agregar_productos', egreso_id=egreso_id)
    productos = Producto.objects.all()
    return render(request, 'agregar_productos.html', {'egreso': egreso, 'productos': productos})
