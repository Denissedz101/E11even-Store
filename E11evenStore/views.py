# ------------- VIEWS.PY ---------------------

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LoginForm
from .models import Administrativo
from .models import Cliente
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Producto, Compra, DetalleCompra
from .forms import DireccionEnvioForm, MetodoPagoForm
import random
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditarClienteForm
from django.contrib.admin.views.decorators import staff_member_required
from .serializers import ProductoSerializer, CompraSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .decorators import cliente_login_required
from .decorators import admin_login_required
from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages



def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario_registro(request):
    form = RegistroForm()

def carro_compras(request):
    return render(request, 'carro_compras.html')

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

# INICIO SESION COMUN
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

# REGISTRO FORMULARIO CLIENTES
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

#CARRITOS COMPRAS
@cliente_login_required
def carrito_compras(request):
    if request.method == 'POST':
        form_direccion = DireccionEnvioForm(request.POST)
        form_pago = MetodoPagoForm(request.POST)
        if form_direccion.is_valid() and form_pago.is_valid():
            carrito = request.session.get('carrito', [])
            if not carrito:
                messages.error(request, "Tu carrito está vacío.")
                return redirect('carro_compras')

            numero_compra = f"E11-{random.randint(100000, 999999)}"
            email_cliente = request.session.get('email_cliente')

            try:
                cliente = Cliente.objects.get(email=email_cliente)
            except Cliente.DoesNotExist:
                messages.error(request, "Cliente no válido.")
                return redirect('inicio')

            compra = Compra.objects.create(
                cliente=cliente,
                numero_compra=numero_compra,
                direccion_envio=form_direccion.cleaned_data['direccion'],
                metodo_pago=form_pago.cleaned_data['metodo_pago'],
                estado='pendiente'
            )

            total = 0
            for item in carrito:
                producto = Producto.objects.get(id=item['producto_id'])
                cantidad = item['cantidad']
                DetalleCompra.objects.create(
                    compra=compra,
                    producto=producto,
                    cantidad=cantidad
                )
                total += producto.precio * cantidad

            total += 3990  # Envío fijo

            send_mail(
                'Confirmación de compra - E11ven Store',
                f'Tu número de compra es {numero_compra}. Total: ${total}. Dirección: {compra.direccion_envio}',
                'E11venStore@gmail.com',
                [cliente.email],
                fail_silently=True
            )

            request.session['carrito'] = []  # Limpiar carrito
            messages.success(request, f'Compra {numero_compra} confirmada ✅')
            return render(request, 'compra_exitosa.html', {
                'compra': compra,
                'total': total,
            })
    else:
        form_direccion = DireccionEnvioForm()
        form_pago = MetodoPagoForm()

    return render(request, 'carrito_compras.html', {
        'form_direccion': form_direccion,
        'form_pago': form_pago
    })


# PANEL ADMINISTRACION
@admin_login_required
def login_admin(request):
    # Variables para cada pestaña
    productos = Producto.objects.all().order_by('nombre', 'categoria')
    compras_recientes = Compra.objects.all().order_by('-fecha')[:10]  # Últimas 10 compras
    historial = []
    cliente = None

    if request.method == 'POST' and 'nombre' in request.POST:
        nombre = request.POST.get('nombre')
        precio = int(request.POST.get('precio'))
        categoria = request.POST.get('categoria')
        stock = int(request.POST.get('stock'))
        imagen = request.FILES.get('imagen')

        producto_existente = Producto.objects.filter(nombre=nombre, categoria=categoria).first()
        if producto_existente:
            producto_existente.stock += stock
            producto_existente.precio = precio
            if imagen:
                producto_existente.imagen = imagen
            producto_existente.save()
            messages.success(request, 'Stock actualizado para producto existente.')
        else:
            Producto.objects.create(nombre=nombre, precio=precio, categoria=categoria, stock=stock, imagen=imagen)
            messages.success(request, 'Producto agregado correctamente.')

    elif request.method == 'POST' and 'rut' in request.POST:
        rut = request.POST.get('rut')
        try:
            cliente = Cliente.objects.get(rut=rut)
            historial = Compra.objects.filter(cliente=cliente).order_by('-fecha')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente no encontrado')

    return render(request, 'login_admin.html', {
        'productos': productos,
        'compras_recientes': compras_recientes,
        'compras': historial,
        'cliente': cliente,
    })


# API REST
@api_view(['GET'])
def api_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_mis_compras(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return Response({'error': 'No autenticado'}, status=401)

    compras = Compra.objects.filter(cliente_id=cliente_id)
    serializer = CompraSerializer(compras, many=True)
    return Response(serializer.data)
    

# ACTUALIZACION DATOS CLIENTES
@cliente_login_required
def login_cliente(request):
    email = request.session.get('email_cliente')

    if not email:
        messages.error(request, "Debes iniciar sesión para acceder.")
        return redirect('inicio_sesion')

    try:
        cliente = Cliente.objects.get(email=email)
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente no encontrado.")
        return redirect('inicio_sesion')

    compras = Compra.objects.filter(cliente=cliente).order_by('-fecha')

    # Calcular totales para cada compra
    compras_con_totales = []
    for compra in compras:
        total = sum(detalle.subtotal for detalle in compra.detalles.all())
        compras_con_totales.append({
            'compra': compra,
            'total': total,
        })

    if request.method == 'POST':
        form = EditarClienteForm(request.POST, instance=cliente)
        pass_form = PasswordChangeForm(user=request.user, data=request.POST)

        if 'guardar_datos' in request.POST and form.is_valid():
            form.save()
            messages.success(request, "Datos actualizados correctamente")
        elif 'cambiar_contraseña' in request.POST and pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, "Contraseña actualizada")
        else:
            messages.error(request, "Error al guardar los cambios")
    else:
        form = EditarClienteForm(instance=cliente)
        pass_form = PasswordChangeForm(user=request.user)

    return render(request, 'login_cliente.html', {
        'cliente': cliente,
        'compras_con_totales': compras_con_totales,
        'form': form,
        'pass_form': pass_form,
    })


# VISTA DE PAGO POR WEBPAY SIMULADA 
@login_required
def redirigir_webpay(request):
    # Simulación: redirigir a una URL de prueba de WebPay
    return redirect('https://webpay3g.transbank.cl/webpay-server/initTransaction')
