from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.cliente.models import Cliente

# Create your models here.
class Usuario(models.Model):
    
    ruc=models.CharField(unique=True,max_length=12)
    razon_social = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)    
    activo = models.BooleanField(default=False)
    usuario_login = models.OneToOneField(User, on_delete=models.PROTECT,null=True)
    # cliente=models.ManyToManyField(Cliente)
    

    def __str__(self):
        return self.nombres

    @property
    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)
