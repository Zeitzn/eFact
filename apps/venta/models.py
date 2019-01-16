from django.db import models
from apps.factura.models import Factura
from apps.producto.models import Producto
# Create your models here.
class Detalle_venta(models.Model):
    
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT,null=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT,null=True)
    cantidad= models.DecimalField(max_digits=18, decimal_places=2)
    monto_total= models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.factura

    @property
    def p_factura(self):
        return '%s %s %s' % (self.factura)
