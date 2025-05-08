from .models import Producto
from .models import Cliente
import requests
from django.conf import settings
from django.core.cache import cache


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

# web service externo APIS
def vista_externa(request):
    # Intenta obtener datos en caché
    juegos = cache.get("juegos_populares")
    noticias = cache.get("noticias_videojuegos")

    # Si no están en caché, realiza las peticiones
    if not juegos:
        try:
            response = requests.get(
                "https://api.rawg.io/api/games",
                params={"key": settings.RAWG_API_KEY, "ordering": "-rating", "page_size": 6},
            )
            if response.status_code == 200:
                juegos = response.json().get("results", [])
                cache.set("juegos_populares", juegos, timeout=3600)  # 1 hora
        except Exception as e:
            print("Error cargando juegos:", e)
            juegos = []

    if not noticias:
        try:
            response = requests.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": "videojuegos",
                    "apiKey": settings.NEWS_API_KEY,
                    "language": "es",
                    "pageSize": 6,
                },
            )
            if response.status_code == 200:
                noticias = response.json().get("articles", [])
                cache.set("noticias_videojuegos", noticias, timeout=1800)  # 30 minutos
        except Exception as e:
            print("Error cargando noticias:", e)
            noticias = []

    return {"juegos": juegos, "noticias": noticias}
