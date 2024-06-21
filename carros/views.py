from django.shortcuts import render, redirect, get_object_or_404
from .models import Egreso, ProductosEgreso
from products.models import Producto
from .forms import AddItemCarroForm, EgresoForm, EditItemCarroForm
from django.contrib import messages
from django.http import JsonResponse

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
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            precio = producto.precio_venta
            subtotal = cantidad * precio
            ProductosEgreso.objects.create(egreso=egreso, producto=producto, cantidad=cantidad, precio=precio, subtotal=subtotal)
            return redirect('agregar_productos', egreso_id=egreso.id)
    else:
        form_add = AddItemCarroForm()
        form_edit = EditItemCarroForm()

    return render(request, 'agregar_productos.html', {
        'egreso': egreso,
        'productos_egreso': productos_egreso,
        'form_add': form_add,
        'form_edit': form_edit
    })

def eliminar_producto(request, item_id):
    producto_egreso = get_object_or_404(ProductosEgreso, id=item_id)
    egreso_id = producto_egreso.egreso.id
    producto_egreso.delete()
    return redirect('agregar_productos', egreso_id=egreso_id)

def editar_producto(request, item_id):
    producto = get_object_or_404(ProductosEgreso, pk=item_id)
    if request.method == 'POST':
        form = EditItemCarroForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto editado exitosamente")
        else:
            messages.error(request, "Error al editar el producto")
    return redirect('agregar_productos', egreso_id=producto.egreso.id)

def buscar_productos(request):
    if 'q' in request.GET:
        query = request.GET['q']
        productos = Producto.objects.filter(nombre__icontains=query)
        results = []
        for producto in productos:
            results.append({
                'id': producto.id,
                'nombre': producto.nombre
            })
        return JsonResponse(results, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)


def guardar_carro(request, egreso_id):
    egreso = get_object_or_404(Egreso, id=egreso_id)
    egreso.usado = True
    egreso.save()
    messages.success(request, "Carro guardado y marcado como usado exitosamente.")
    return redirect('listar_egresos')
