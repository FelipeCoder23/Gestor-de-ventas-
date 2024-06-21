from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_carros, name='listar_carros'),
    path('realizar_venta/<int:egreso_id>/', views.realizar_venta, name='realizar_venta'),
    path('ventas_diarias/', views.ventas_diarias, name='ventas_diarias'),
]
