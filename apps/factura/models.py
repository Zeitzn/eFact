from django.db import models
from apps.usuario.models import Usuario
from apps.cliente.models import Cliente
# Create your models here.
class Factura(models.Model):
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True)
    fecha_emision = models.DateTimeField(blank=True, null=False)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    numero_factura=models.CharField(max_length=12)
    

    def __str__(self):
        return self.numero_factura

    @property
    def p_numero_factura(self):
        return '%s %s %s' % (self.numero_factura)
