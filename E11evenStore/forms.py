from django import forms
from .models import Cliente
from .models import Administrativo
from django.core.exceptions import ValidationError
import re

# inicio sesion clientes/admin
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'required': 'required'
        })
    )
    
    clave = forms.CharField(
        label='clave',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'clave',
            'required': 'required'
        })
    )

# Formulario registro clientes
class RegistroForm(forms.ModelForm):
    repetir_clave = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = ['usuario', 'nombre', 'apellidos', 'rut', 'email', 'clave', 'fechaNacimiento', 'direccion']
        widgets = {
            'clave': forms.PasswordInput(),
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not re.match(r'^\d{7,8}-[\dkK]$', rut):
            raise ValidationError("El RUT debe tener el formato 12345678-9")
        return rut

    def clean(self):
        cleaned_data = super().clean()
        clave = cleaned_data.get("clave")
        repetir_clave = cleaned_data.get("repetirClave")
        if clave != repetir_clave:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data