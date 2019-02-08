from django.shortcuts import render
from django.http import HttpResponse
from apps.producto.models import Producto
from apps.establecimiento.models import Establecimiento
from apps.cliente.models import Cliente
from apps.usuario.models import Usuario
from apps.venta.models import Detalle_venta
from apps.factura.models import Factura
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
import simplejson as json

def index(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    oFactura=Factura.objects.filter(usuario_id=oUsuario.id)

    oDetalle_venta=Detalle_venta.objects.filter(factura_id__in=[p.id for p in oFactura])

    context={
        'ventas':oDetalle_venta,
        'facturas':oFactura,
        }


    return render(request,'venta/index.html',context)


def generarVenta(request):

    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    oProductos=Producto.objects.all()
    oEstablecimientos=Establecimiento.objects.filter(
        usuario=oUsuario
        )
    context={
        'productos':oProductos,
        'establecimientos':oEstablecimientos,
    }
    return render(request,'venta/generar.html',context)


@csrf_exempt
def registrarFactura(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    if request.method=='POST':
        Datos=json.loads(request.body)

        ruc_cliente=Datos[0]['datos']['cliente_ruc_dni']
        # print(ruc_cliente)

        oCliente=Cliente.objects.get(ruc=ruc_cliente)

        factura=Factura(
            usuario=oUsuario,
            cliente=oCliente,
            numero_factura='FA-0000001'
        )
        factura.save()

    return HttpResponse(str("success"))

