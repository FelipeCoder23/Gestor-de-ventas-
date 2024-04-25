from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto
from .forms import Editarinventarioform,AddProductoForm,SimpleProductoForm
from pyexpat.errors import messages


# Create your views here.


def productos_view(request):
    productos =  Producto.objects.all()
    form_productos = AddProductoForm()
    form_edit = Editarinventarioform()


    context = {
        "productos" : productos,
        "form_personal": form_productos,
        "form_edit" : form_edit,
    }
    return render( request,'products/productos.html',context)

def add_producto(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"error al guarda el producto")
                return redirect('productos_view')

    return redirect('productos_view')

def Deleteproducto3(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get("id_producto_eliminar"))
        producto.delete()
    return redirect('productos_view')

def edit_producto(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get("id_producto_editar"))
        form =Editarinventarioform(request.POST,request.FILES,instance=producto)
        if form.is_valid:
            form.save()
    return redirect('productos_view')

def Addproducto(request):
    productos =  Producto.objects.all()
    form_personal = AddProductoForm()
    form_edit = Editarinventarioform()
    form_personal = SimpleProductoForm()
    context = {
        "productos": productos,
        "form_personal": form_personal,
        "form_edit": form_edit,
        "form": form_personal,
    }	
    return render(request, 'products/productos.html', context)


def Addproducto3(request):
    if request.method == 'POST':
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Addproducto')  # Redirecciona de nuevo a la página de productos
    else:
        form = AddProductoForm()

    productos = Producto.objects.all()
    context = {
        "productos": productos,
        "form_add": form
    }   
    return render(request, 'products/productos.html', context)

def edit_producto_view(request):
    print("entro a editar_producto_view")
    if request.POST:
        print("entro if")
        producto = Producto.objects.get(pk=request.POST.get('id_producto_editar'))
        print("paso producto")
        form = Editarinventarioform(
            request.POST, request.FILES, instance= producto)
        print("paso form")
        if form.is_valid():
            form.save()
        print("pàso todo")    
    return render(request, 'products/productos.html')

def Deleteproducto2(request):
    if request.method == 'POST':
        producto_id = request.POST.get("id_producto_eliminar")

        if producto_id:
            # Usando get_object_or_404, si el producto no existe, se devolverá automáticamente una página de error 404.
            producto = get_object_or_404(Producto, pk=producto_id)
            producto.delete()
            # Puedes agregar un mensaje de éxito aquí si estás usando el framework de mensajes.
        else:
            # Puedes agregar un mensaje de error aquí si estás usando el framework de mensajes.
            pass

    return redirect('Addproducto')  # Asumo que 'Addproducto' es el nombre correcto de tu URL.




def webeo(request):

    return redirect( 'products/productos.html')




def Editproducto(request):
    print("entro a editar")
    
    if request.method == 'POST':
        print("entro a post")
        print(request.POST)
        producto_id = request.POST.get('id_producto_editar')
        print(producto_id)
        
        if not producto_id.isdigit():
            print("producto_id no es un número válido:", producto_id)
        
        producto = get_object_or_404(Producto, pk=int(producto_id))
        print("paso producto")
        print("antes de form")
        form = Editarinventarioform(request.POST, request.FILES, instance=producto)
        print("paso form")

        if form.is_valid():
            print("entro a valid")
            form.save()
            print("guardado")
            return redirect('Addproducto')  # Redirecciona de nuevo a la página de productos después de editar

    else:
        print("entro a else")
        form = Editarinventarioform()

    # Aquí insertaremos la línea para imprimir los campos del formulario
    print("Campos del formulario:", form.fields)
    
    productos = Producto.objects.all()
    context = {
        "productos": productos,
        "form_edit": form,
    }   
    
    return render(request, 'products/productos.html', context)




def EditProductoSimple(request):
    if request.method == 'POST':
        form = SimpleProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Addproducto')
    else:
        form = SimpleProductoForm()

    context = {
        "form": form,
    }
    return render(request, 'products/productos.html', context)



def simple_producto_view(request):
    form = SimpleProductoForm()
    form_personal = AddProductoForm()

    if request.method == 'POST':
        form = SimpleProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir o hacer lo que necesites después de guardar el formulario

    context = {
        
        "form_add": form_personal,
        'simple_form': form,
    }

    return render(request,'productos/simple_producto.html', context)



def add_cliente_view(request):
    #print("Guardar cliente")
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try: 
                form.save()
            except:
                messages(request, "Error al guardar el cliente")
                return redirect('productos')
    return redirect('productos')