from django.shortcuts import render, redirect, get_object_or_404
from .models import Egreso, ProductosEgreso
from products.models import Producto
from .forms import AddItemCarroForm, EgresoForm, EditItemCarroForm
from django.contrib import messages

def listar_egresos(request):
    egresos = Egreso.objects.filter(usado=False)
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

def asignar_carro(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    egreso.usado = True
    egreso.save()
    return redirect('agregar_productos', egreso_id=egreso_id)
def agregar_productos(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    productos_egreso = ProductosEgreso.objects.filter(egreso=egreso)

    if request.method == 'POST':
        form = AddItemCarroForm(request.POST)
        if form.is_valid():
            producto_egreso = form.save(commit=False)
            producto_egreso.egreso = egreso
            producto_egreso.save()
            messages.success(request, "Producto agregado exitosamente")
            return redirect('agregar_productos', egreso_id=egreso.id)
        else:
            messages.error(request, "Error al agregar el producto")
    else:
        form = AddItemCarroForm()

    productos = Producto.objects.all()
    return render(request, 'agregar_productos.html', {'egreso': egreso, 'productos': productos, 'productos_egreso': productos_egreso, 'form_add': form})

def editar_producto(request, item_id):
    item = get_object_or_404(ProductosEgreso, id=item_id)
    if request.method == 'POST':
        form = EditItemCarroForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto editado exitosamente")
            return redirect('agregar_productos', egreso_id=item.egreso.id)
        else:
            messages.error(request, "Error al editar el producto")
    else:
        form = EditItemCarroForm(instance=item)
    return render(request, 'editar_producto.html', {'form_edit': form, 'item': item})

def eliminar_producto(request, item_id):
    item = get_object_or_404(ProductosEgreso, id=item_id)
    egreso_id = item.egreso.id
    item.delete()
    messages.success(request, "Producto eliminado del carro exitosamente")
    return redirect('agregar_productos', egreso_id=egreso_id)
