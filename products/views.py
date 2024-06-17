

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import Editarinventarioform, AddProductoForm
from django.contrib import messages

# Vista para mostrar los productos
def productos_view(request):
    productos = Producto.objects.all()
    form_productos = AddProductoForm()
    form_edit = Editarinventarioform()

    context = {
        "productos": productos,
        "form_add": form_productos,
        "form_edit": form_edit,
    }
    return render(request, 'products/productos.html', context)

# Vista para agregar un producto
def add_producto(request):
    if request.method == 'POST':
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Producto agregado exitosamente")
            except:
                messages.error(request, "Error al guardar el producto")
        else:
            messages.error(request, "Formulario inválido")
    return redirect('productos_view')

# Vista para eliminar un producto
def delete_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get("id_producto_eliminar")
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        messages.success(request, "Producto eliminado exitosamente")
    return redirect('productos_view')

# Vista para editar un producto
def edit_producto(request):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=request.POST.get('id_producto_editar'))
        form = Editarinventarioform(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto editado exitosamente")
        else:
            messages.error(request, "Error al editar el producto")
    return redirect('productos_view')
