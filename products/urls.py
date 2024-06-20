
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_producto, name='add_producto'),
    path('edit/', views.edit_producto, name='edit_producto'),
    path('delete/', views.delete_producto, name='delete_producto'),
    path('', views.productos_view, name='productos_view'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('desactivar_producto/<int:producto_id>/', views.desactivar_producto, name='desactivar_producto'),
    path('activar_producto/<int:producto_id>/', views.activar_producto, name='activar_producto'),
]
