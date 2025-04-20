from .models import Producto
from .models import Cliente


def contador_carro(request):
    carro = request.session.get("carro", [])
    total_items = sum(item["cantidad"] for item in carro)
    total_precio = 0
    for item in carro:
        try:
            producto = Producto.objects.get(id=item["producto_id"])
            total_precio += producto.precio * item["cantidad"]
        except Producto.DoesNotExist:
            pass
    return {"contador_carro": total_items, "precio_carro": total_precio}


def cliente_context(request):
    email = request.session.get("email_cliente")
    cliente = None
    if email:
        try:
            cliente = Cliente.objects.get(email=email)
        except Cliente.DoesNotExist:
            pass
    return {"cliente": cliente}
