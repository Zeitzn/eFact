from django.db import models

# Create your models here.
class Producto(models.Model):
    
    
    nombre = models.CharField(max_length=200)
    precio_unitario = models.DecimalField(max_digits=18, decimal_places=2)
    # ruc_usuario=models.CharField(max_length=12)
    

    def __str__(self):
        return self.nombre

    @property
    def p_nombre(self):
        return '%s %s %s' % (self.nombre)
