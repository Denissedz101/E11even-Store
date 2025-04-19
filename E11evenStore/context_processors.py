from .models import Producto


def contador_carro(request):
    carro = request.session.get('carro', [])
    total_items = sum(item['cantidad'] for item in carro)
    total_precio = 0
    for item in carro:
        try:
            producto = Producto.objects.get(id=item['producto_id'])
            total_precio += producto.precio * item['cantidad']
        except Producto.DoesNotExist:
            pass  
    return {
        'contador_carro': total_items,
        'precio_carro': total_precio
    }
