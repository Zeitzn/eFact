from rest_framework import serializers
from apps.establecimiento.models import Establecimiento

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Establecimiento
        fields=('id','usuario','direccion','tipo_establecimiento','ubigeo')