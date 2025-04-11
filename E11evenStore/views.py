from django.shortcuts import render
from django.http import JsonResponse
from .models import Carrito 

def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario_registro(request):
    return render(request, 'formulario_registro.html')

def carro_compras(request):
    return render(request, 'carro_compras.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def menu_categorias(request):
    return render(request, 'menu_categorias.html')

def modif_datos_usuario(request):
    return render(request, 'modif_datos_usuario.html')

def panel_admin(request):
    return render(request, 'panel_admin.html')
    
    # categorias menu #
def accion(request):
    return render(request, 'accion.html')

def carreras(request):
    return render(request, 'carreras.html')

def free_to_play(request):
    return render(request, 'free_to_play.html')

def mundo_abierto(request):
    return render(request, 'mundo_abierto.html')

def supervivencia(request):
    return render(request, 'supervivencia.html')

def terror(request):
    return render(request, 'terror.html')

#contador carrito

def contador_carrito(request):
    total = Carrito.objects.filter(usuario=request.user).count()
    return JsonResponse({'total': total})

