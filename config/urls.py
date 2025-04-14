
from django.contrib import admin
from django.urls import path
from E11evenStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.formulario_registro, name='formulario_registro'),
    path('carro/', views.carro_compras, name='carro_compras'),
    path('inicio_sesion', views.inicio_sesion, name='inicio_sesion'),
    path('categorias/', views.menu_categorias, name='menu_categorias'),
    path('login_cliente/', views.login_cliente, name='login_cliente'),
    path('login_admin/', views.login_admin, name='login_admin'),

    # Categorías
    path('accion/', views.accion, name='accion'),
    path('carreras/', views.carreras, name='carreras'),
    path('free/', views.free_to_play, name='free_to_play'),
    path('mundo-abierto/', views.mundo_abierto, name='mundo_abierto'),
    path('supervivencia/', views.supervivencia, name='supervivencia'),
    path('terror/', views.terror, name='terror'),

    #carrito
    path('contador-carrito/', views.contador_carrito, name='contador_carrito'),
]
