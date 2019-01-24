from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from apps.producto.models import Producto
from django.views.decorators.csrf import csrf_exempt
from apps.usuario.models import Usuario
import json

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from apps.producto.serializers import ProductoSerializer
# Create your views here.


# def index(request):
    # if request.user.is_authenticated:
    #     oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)        
    # else:
    #     oUsuario = ''

    # oProductos=Producto.objects.all()

    # context={
    #     'productos':oProductos,
    # }
    # # try:
    # if request.method=='POST':        
    #     form=Producto(
    #         nombre=request.POST['nombre'],
    #         precio_unitario=request.POST['precio_unitario'],
    #         # ruc_usuario=oUsuario.ruc
    #         )
    #     form.save()
    #     messages.add_message(request, messages.INFO, "El registro fue agregado con éxito.")
    #     # return redirect('producto:index')        
    #     return render(request,'producto/index.html',context)
    # else:
    #     form='' 
    # # finally:
    # return render(request,'producto/index.html',context)



# @csrf_exempt
# def update(request):
#     id=request.POST['id']
#     precio=request.POST['precio']
#     nombre=request.POST['nombre']
    
#     oProducto=Producto.objects.get(id=id)

#     print(request.POST['precio'])

#     v_precio = precio.replace(',', '.')

#     oProducto.nombre=nombre
#     oProducto.precio_unitario=float(v_precio)

#     oProducto.save()

#     return render(request,'producto/index.html')

# @csrf_exempt
# def delete(request):
#     id=request.POST['id']
#     oProducto=Producto.objects.get(id=id)
#     oProducto.delete()
#     return render(request,'producto/index.html')


#----------USANDO API REST-------------

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return render(request,'producto/index.html')

# @csrf_exempt
# def list(request):
#     oProductos=Producto.objects.all()
#     serializer=ProductoSerializer(oProductos,many=True)

#     return JSONResponse(serializer.data)

class ListView(generics.ListAPIView):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer

@csrf_exempt
def create(request):
    data=JSONParser().parse(request)
    serializer=ProductoSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def update(request,pk):

    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)

    data = JSONParser().parse(request)
    serializer = ProductoSerializer(producto, data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def delete(request,pk):
    try:
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return HttpResponse(status=204)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    