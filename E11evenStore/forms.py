from django import forms
from .models import Cliente
from .models import Administrativo

class LoginForm(forms.Form):
    correo = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo',
            'required': 'required'
        })
    )
    
    contraseña = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )


