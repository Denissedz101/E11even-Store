from django.contrib import admin
from .models import Cliente
from .models import Administrativo


class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'rut', 'email',)
    search_fields = ('nombre','apellidos', 'rut',)
 
    
class AdministrativoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'rut', 'email',)
    search_fields = ('nombre','apellidos', 'rut',)
    
    
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Administrativo, AdministrativoAdmin)

