from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto} x{self.cantidad} - {self.usuario.username}"