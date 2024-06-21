from django.urls import path
from . import views

urlpatterns = [
    path('listar_egresos/', views.listar_egresos, name='listar_egresos'),
    path('detalle_egreso/<int:egreso_id>/', views.detalle_egreso, name='detalle_egreso'),
    path('agregar_item_egreso/<int:egreso_id>/', views.agregar_item_egreso, name='agregar_item_egreso'),
    path('eliminar_item_carro/<int:item_id>/', views.eliminar_item_carro, name='eliminar_item_carro'),
    path('asignar_carro/<int:egreso_id>/', views.asignar_carro, name='asignar_carro'),
    path('agregar_productos/<int:egreso_id>/', views.agregar_productos, name='agregar_productos'),
    path('eliminar_producto/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:item_id>/', views.editar_producto, name='editar_producto'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('carros/guardar_carro/<int:egreso_id>/', views.guardar_carro, name='guardar_carro'),

]
