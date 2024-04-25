from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.login_user , name='register'),
    path('', views.signin, name='login'),
    path('logout/', views.signin, name='logout'),
    path('jefe/', views.jefe, name='jefe'),
    path('empleado/', views.empleado, name='empleado'),
    path('signin/', views.signin, name='signin'),
    #... y cualquier otra URL que quieras definir para la app users.
]


