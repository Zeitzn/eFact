from django.db import models

from apps.establecimiento.models import Establecimiento
# Create your models here.
class Producto(models.Model):
    UNIDADES = (
        ('barriles', 'barriles'),
        ('cajas', 'cajas'),
        ('galones', 'galones'),
        ('gramos', 'gramos'),
        ('kilogramos', 'kilogramos'),
        ('latas', 'latas'),
        ('libras', 'libras'),
        ('litros', 'litros'),
        ('metros', 'metros'),
        ('metros cúbicos', 'metros cúbicos'),
        ('millares', 'millares'),
        ('toneladas cortas', 'toneladas cortas'),
        ('toneladas largas', 'toneladas largas'),
        ('toneladas métricas', 'toneladas métricas'),        
        ('unidades', 'unidades')        
    )
    
    nombre = models.CharField(max_length=200)
    precio_unitario = models.DecimalField(max_digits=18, decimal_places=2)
    unidad=models.CharField(max_length=50, choices=UNIDADES)
    # ruc_usuario=models.CharField(max_length=12)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT,null=True)

    

    def __str__(self):
        return self.nombre

    @property
    def p_nombre(self):
        return '%s %s %s' % (self.nombre)
