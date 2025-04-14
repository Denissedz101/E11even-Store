from django.db import models
from django.contrib.auth.models import User

# Registro compras
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto} x{self.cantidad} - {self.usuario.username}"
    
# Registro usuarios 
class Cliente(models.Model):
    rut = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    usuario = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    clave = models.CharField(max_length=128)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'E11EVENSTORE_CLIENTES'

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellidos}"

# Registro administrativos
class Administrativo(models.Model):
    rut = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    usuario = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    clave = models.CharField(max_length=128)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'E11EVENSTORE_ADMINISTRATIVOS'

    def __str__(self):
        return f"Administrativo: {self.nombre} {self.apellidos}"