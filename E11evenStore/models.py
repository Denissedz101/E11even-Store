from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto} x{self.cantidad} - {self.usuario.username}"
    
# Registro usuarios y administrativos

class Usuario (models.Model):
    TIPO_USUARIO_CHOICES = [
        ('usuario', 'Usuario'),
        ('admin', 'Administrativo'),
    ]

    rut = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    usuario = models.CharField(max_length=150)
    correo = models.EmailField(primary_key=True)
    contraseña = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.tipo_usuario})"