
from django.contrib import admin
from django.urls import path
from E11evenStore import views
from django.conf import settings
from django.conf.urls.static import static

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
    
     # API
    path('api/productos/', views.api_productos, name='api_productos'),
    path('api/mis-compras/', views.api_mis_compras, name='api_mis_compras'),

    # Categorías
    path('categoria_accion/', views.categoria_accion, name='accion'),
    path('categoria_carreras/', views.categoria_carreras, name='carreras'),
    path('categoria_free_to_play/', views.categoria_free_to_play, name='free_to_play'),
    path('categoria_mundo_abierto/', views.categoria_mundo_abierto, name='mundo_abierto'),
    path('categoria_supervivencia/', views.categoria_supervivencia, name='supervivencia'),
    path('categoria_terror/', views.categoria_terror, name='terror'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)