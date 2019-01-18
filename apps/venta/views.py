from django.shortcuts import render

from apps.producto.models import Producto
from apps.establecimiento.models import Establecimiento
from apps.usuario.models import Usuario
from apps.venta.models import Detalle_venta
from apps.factura.models import Factura
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    oFactura=Factura.objects.filter(usuario_id=oUsuario.id)

    oDetalle_venta=Detalle_venta.objects.filter(factura_id__in=[p.id for p in oFactura])

    context={
        'ventas':oDetalle_venta,
        }


    return render(request,'venta/index.html',context)


def generate(request):

    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    oProductos=Producto.objects.filter(ruc_usuario=oUsuario.ruc)
    oEstablecimientos=Establecimiento.objects.filter(
        usuario=oUsuario
        )
    context={
        'productos':oProductos,
        'establecimientos':oEstablecimientos,
    }
    return render(request,'venta/generar.html',context)
