from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from apps.producto.models import Producto
from django.views.decorators.csrf import csrf_exempt
from apps.usuario.models import Usuario
import json
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    else:
        oUsuario = ''

    oProductos=Producto.objects.all()

    context={
        'productos':oProductos,
    }
    # try:
    if request.method=='POST':        
        form=Producto(
            nombre=request.POST['nombre'],
            precio_unitario=request.POST['precio_unitario'],
            ruc_usuario=oUsuario.ruc
            )
        form.save()
        messages.add_message(request, messages.INFO, "El registro fue agregado con éxito.")
        # return redirect('producto:index')        
        return render(request,'producto/index.html',context)
    else:
        form='' 
    # finally:
    return render(request,'producto/index.html',context)

@csrf_exempt
def update(request):
    id=request.POST['id']
    precio=request.POST['precio']
    nombre=request.POST['nombre']
    
    oProducto=Producto.objects.get(id=id)

    print(request.POST['precio'])

    v_precio = precio.replace(',', '.')

    oProducto.nombre=nombre
    oProducto.precio_unitario=float(v_precio)

    oProducto.save()

    return render(request,'producto/index.html')

@csrf_exempt
def delete(request):
    id=request.POST['id']
    oProducto=Producto.objects.get(id=id)
    oProducto.delete()
    return render(request,'producto/index.html')
