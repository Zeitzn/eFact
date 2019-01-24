from django.shortcuts import render
from django.http import HttpResponse
from apps.establecimiento.models import Establecimiento
from apps.usuario.models import Usuario
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from apps.establecimiento.serializers import EstablecimientoSerializer
# Create your views here.
# def index(request):
#     if request.user.is_authenticated:
#         oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
#     else:
#         oUsuario=''

#     oEstablecimientos=Establecimiento.objects.all()

#     context={
#         'establecimientos':oEstablecimientos,
#     }
#     # try:
#     if request.method=='POST':        
#         form=Establecimiento(
#             direccion=request.POST['direccion'],
#             tipo_establecimiento=request.POST['tipo_establecimiento'],
#             ubigeo=request.POST['ubigeo'],
#             usuario=oUsuario
#             )
#         form.save()
#         messages.add_message(request, messages.INFO, "El registro fue agregado con éxito.")
#         # return redirect('producto:index')        
#         return render(request,'establecimiento/index.html',context)
#     else:
#         form='' 
#     # finally:
#     return render(request,'establecimiento/index.html',context)
# @csrf_exempt
# def update(request,pk):
#     if request.user.is_authenticated:
#         oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
#     else:
#         oUsuario=''

#     id=request.POST['id']
#     tipo_establecimiento=request.POST['tipo_establecimiento']
#     direccion=request.POST['direccion']
#     ubigeo=request.POST['ubigeo']
    
#     oEstablecimiento=Establecimiento.objects.get(id=id)   

#     oEstablecimiento.tipo_establecimiento=tipo_establecimiento
#     oEstablecimiento.ubigeo=ubigeo
#     oEstablecimiento.direccion=direccion
#     oEstablecimiento.usuario=oUsuario
#     oEstablecimiento.save()

#     return render(request,'establecimiento/index.html')

# @csrf_exempt
# def delete(request):
#     id=request.POST['id']
#     oEstablecimiento=Establecimiento.objects.get(id=id)
#     oEstablecimiento.delete()
#     return render(request,'establecimiento/index.html')

#----------USANDO API REST-------------

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return render(request,'establecimiento/index.html')

class ListView(generics.ListAPIView):
    queryset=Establecimiento.objects.all()
    serializer_class=EstablecimientoSerializer

@csrf_exempt
def create(request):
    # if request.user.is_authenticated:
    #     oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    # else:
    #     oUsuario=''

    # request.POST['usuario']=oUsuario.id

    data=JSONParser().parse(request)
    serializer=EstablecimientoSerializer(data=data)
    # print(request.POST['usuario'])
    if serializer.is_valid():
        serializer.save()
        
        return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def update(request,pk):

    try:
        establecimiento = Establecimiento.objects.get(pk=pk)
    except Establecimiento.DoesNotExist:
        return HttpResponse(status=404)

    data = JSONParser().parse(request)
    serializer = EstablecimientoSerializer(establecimiento, data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def delete(request,pk):
    try:
        establecimiento = Establecimiento.objects.get(pk=pk)
        establecimiento.delete()
        return HttpResponse(status=204)
    except Establecimiento.DoesNotExist:
        return HttpResponse(status=404)
    