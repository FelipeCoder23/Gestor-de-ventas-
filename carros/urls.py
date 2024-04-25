from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('add_venta/', views.add_ventas.as_view(), name='AddVenta'),
    
    
    # ... otras rutas que puedas tener ...
]
