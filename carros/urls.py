from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listar_egresos/', views.listar_egresos, name='listar_egresos'),
    path('egreso/<int:egreso_id>/', views.detalle_egreso, name='detalle_egreso'),
    path('egreso/<int:egreso_id>/agregar/', views.agregar_item_egreso, name='agregar_item_egreso'),
    path('item/<int:item_id>/eliminar/', views.eliminar_item_carro, name='eliminar_item_carro'),
]
