from django.shortcuts import render

from apps.producto.models import Producto
from apps.establecimiento.models import Establecimiento
from apps.usuario.models import Usuario
# Create your views here.
def index(request):

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
    return render(request,'home/index.html',context)
