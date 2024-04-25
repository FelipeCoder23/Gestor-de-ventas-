from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('empleado', 'Empleado'),
        ('jefe', 'Jefe/Caja'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='empleado')
