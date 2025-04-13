from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Carrito 
from .forms import LoginForm
from .models import Administrativo
from .models import Cliente

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

def login_cliente(request):
    return render(request, 'login_cliente.html')

def login_admin(request):
    return render(request, 'login_admin.html')
    
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

# login_cliente
def inicio_sesion(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            try:
                usuario_cliente = Cliente.objects.get(correo=correo, contraseña=contraseña)
                return redirect('login_cliente') 
            except Cliente.DoesNotExist:
                form.add_error(None, "Usuario no encontrado o datos incorrectos.")
    
    return render(request, 'inicio_sesion.html', {'form': form})

# inicio sesion

def inicio_sesion(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            es_admin = request.POST.get("es_admin")  # ← valor "1" si es admin

            if es_admin == "1":
                # Login como administrador
                try:
                    usuario_admin = Administrativo.objects.get(correo=correo, contraseña=contraseña)
                    return redirect('login_admin')
                except Administrativo.DoesNotExist:
                    form.add_error(None, "Acceso denegado. Administrador no registrado o contraseña incorrecta.")
            else:
                # Login como cliente
                try:
                    usuario_cliente = Cliente.objects.get(correo=correo, contraseña=contraseña)
                    return redirect('login_cliente')
                except Cliente.DoesNotExist:
                    form.add_error(None, "Correo o contraseña incorrectos.")

    return render(request, 'inicio_sesion.html', {'form': form})
