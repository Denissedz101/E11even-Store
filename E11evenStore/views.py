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

def login_cliente(request):
    correo = request.session.get("correo_cliente")

    if not correo:
        return redirect('inicio_sesion')  # Por si intenta entrar sin loguearse

    try:
        cliente = Cliente.objects.get(correo=correo)
    except Cliente.DoesNotExist:
        return redirect('inicio_sesion')

    if request.method == "POST":
        cliente.usuario = request.POST.get("usuario")
        cliente.direccion = request.POST.get("direccion")
        # puedes guardar método de pago aquí si lo tienes en el modelo
        cliente.save()

    return render(request, 'login_cliente.html', {'cliente': cliente})


# inicio sesion

def inicio_sesion(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            es_admin = request.POST.get("es_admin")

            if es_admin == "1":
                try:
                    admin = Administrativo.objects.get(correo=correo, contraseña=contraseña)
                    request.session['correo_admin'] = admin.correo
                    return redirect('login_admin')
                except Administrativo.DoesNotExist:
                    form.add_error(None, "Acceso denegado. Administrador no registrado.")
            else:
                try:
                    cliente = Cliente.objects.get(correo=correo, contraseña=contraseña)
                    request.session['correo_cliente'] = cliente.correo  # 🔐 Aquí lo guardas
                    return redirect('login_cliente')
                except Cliente.DoesNotExist:
                    form.add_error(None, "Correo o contraseña incorrectos.")
    return render(request, 'inicio_sesion.html', {'form': form})


