from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now

class Registro_Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nac = models.DateField()

    def __str__(self):
        return self.user.username

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='')

    def __str__(self):
        return self.nombre
    
