from rest_framework import serializers
from apps.producto.models import Producto
from apps.establecimiento.serializers import EstablecimientoSerializer
class ProductoSerializer(serializers.ModelSerializer):
    # establecimiento=EstablecimientoSerializer(many=True, read_only=True)
    class Meta:
        model=Producto
        fields=('id','nombre','precio_unitario','establecimiento','unidad')