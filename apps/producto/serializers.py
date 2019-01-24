from rest_framework import serializers
from apps.producto.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields=('id','nombre','precio_unitario')