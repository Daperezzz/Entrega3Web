from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Registro_Usuario
from .forms import ProductoForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

def contacto(request):
    return render(request, 'contacto.html')

def quienes_somos(request):
    return render(request, 'QuienesSomos.html')

def carrito(request):
    return render(request, 'carrito.html')

def registrar(request):
    data = {
        'form': SignUpForm()
    }
    
    if request.method == "POST":
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            fecha_nac = formulario.cleaned_data.get('fecha_nac')
            Registro_Usuario.objects.create(user=user, fecha_nac=fecha_nac)
            
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                print("User authenticated and logged in successfully")
                messages.success(request, "Te has registrado correctamente")
                return redirect('home')
            else:
                print("Authentication failed")
                messages.error(request, "Error en la autenticación")
        else:
            print("Form is not valid")
            messages.error(request, "Por favor, corrige los errores en el formulario")
        
        data["form"] = formulario
    
    return render(request, 'registration/registrar.html', data)

@login_required
def pagina_protegida(request):
    return render(request, 'pagina_protegida.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})


def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'editar_producto.html', {'form': form})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})


def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')