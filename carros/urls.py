from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listar_egresos/', views.listar_egresos, name='listar_egresos'),
    path('detalle_egreso/<int:egreso_id>/', views.detalle_egreso, name='detalle_egreso'),
    path('agregar_item_egreso/<int:egreso_id>/', views.agregar_item_egreso, name='agregar_item_egreso'),
    path('eliminar_item_carro/<int:item_id>/', views.eliminar_item_carro, name='eliminar_item_carro'),
    path('asignar_carro/', views.asignar_carro, name='asignar_carro'),
    path('agregar_productos/<int:egreso_id>/', views.agregar_productos, name='agregar_productos'),
]
