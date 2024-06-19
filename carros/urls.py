from django.urls import path
from . import views

urlpatterns = [
    path('listar_egresos/', views.listar_egresos, name='listar_egresos'),
    path('asignar_carro/', views.asignar_carro, name='asignar_carro'),
    path('agregar_productos/<int:egreso_id>/', views.agregar_productos, name='agregar_productos'),
    path('editar_producto/<int:item_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),
]
