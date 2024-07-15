from django import forms # type: ignore
from .models import Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']

class SignUpForm(UserCreationForm):
    fecha_nac= forms.DateField()
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email', 'fecha_nac']
    pass
