
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_producto, name='add_producto'),
    path('edit/', views.edit_producto, name='edit_producto'),
    path('delete/', views.delete_producto, name='delete_producto'),
    path('', views.productos_view, name='productos_view'),
]
