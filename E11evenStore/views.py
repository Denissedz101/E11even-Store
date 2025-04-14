from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Carrito 
from .forms import LoginForm
from .models import Administrativo
from .models import Cliente
from .forms import RegistroForm
from django.contrib import messages


def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario_registro(request):
    form = RegistroForm()
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


# inicio sesion-general

def inicio_sesion(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']
            es_admin = request.POST.get("es_admin")  # Esto nos indica si es admin o cliente
            
            if es_admin == "1":
                try:
                    admin = Administrativo.objects.get(email=email, clave=clave)
                    request.session['email_admin'] = admin.email
                    messages.success(request, "¡Bienvenido Administrador!")
                    return redirect('login_admin')
                except Administrativo.DoesNotExist:
                    form.add_error(None, "Acceso denegado. Administrador no registrado.")
            else:
                try:
                    cliente = Cliente.objects.get(email=email, clave=clave)
                    request.session['email_cliente'] = cliente.email
                    messages.success(request, "¡Bienvenido Cliente!")
                    return redirect('login_cliente')
                except Cliente.DoesNotExist:
                    form.add_error(None, "Correo o contraseña incorrectos.")
    
    return render(request, 'inicio_sesion.html', {'form': form})

# Registro formulario clientes
def formulario_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
            return redirect('inicio_sesion')
    else:
        form = RegistroForm()

    return render(request, 'formulario_registro.html', {'form': form})