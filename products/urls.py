from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('addproducto/', views.Addproducto3, name='Addproducto'),
    path('Editproducto/', views.edit_producto_view, name='Editproducto'),
    path('Deleteproducto/', views.Deleteproducto2, name='Deleteproducto'),
    path('productos2/', views.productos_view, name='productos_view'),
    path('addproducto2/', views.add_producto, name='Addproducto2'),
    path('Deleteproducto2/', views.Deleteproducto3, name='Deleteproducto2'),
    path('Editproducto2/', views.edit_producto, name='Editproducto2'), 
    # ... otras rutas que puedas tener ...
]
