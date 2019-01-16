from django.db import models

from apps.usuario.models import Usuario
# Create your models here.
class Establecimiento(models.Model):
    TIPO_ESTABLECIMIENTO = (
        ('Fiscal', 'Domicilio Fiscal'),
        ('Anexo', 'Anexo'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT,null=True)
    direccion=models.CharField(max_length=255,null=True)
    tipo_establecimiento = models.CharField(max_length=50, choices=TIPO_ESTABLECIMIENTO)
    ubigeo = models.IntegerField() 

    def __str__(self):
        return self.direccion

    @property
    def p_direccion(self):
        return '%s %s %s' % (self.direccion)

