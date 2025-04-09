"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from E11evenStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.formulario_registro, name='formulario_registro'),
    path('carro/', views.carro_compras, name='carro_compras'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('categorias/', views.menu_categorias, name='menu_categorias'),
    path('modificar/', views.modif_datos_usuario, name='modif_datos_usuario'),
    path('admin-panel/', views.panel_admin, name='panel_admin'),

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
