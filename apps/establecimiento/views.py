from django.shortcuts import render
from apps.establecimiento.models import Establecimiento
from apps.usuario.models import Usuario
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''

    oEstablecimientos=Establecimiento.objects.all()

    context={
        'establecimientos':oEstablecimientos,
    }
    # try:
    if request.method=='POST':        
        form=Establecimiento(
            direccion=request.POST['direccion'],
            tipo_establecimiento=request.POST['tipo_establecimiento'],
            ubigeo=request.POST['ubigeo'],
            usuario=oUsuario
            )
        form.save()
        messages.add_message(request, messages.INFO, "El registro fue agregado con éxito.")
        # return redirect('producto:index')        
        return render(request,'establecimiento/index.html',context)
    else:
        form='' 
    # finally:
    return render(request,'establecimiento/index.html',context)
@csrf_exempt
def update(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''

    id=request.POST['id']
    tipo_establecimiento=request.POST['tipo_establecimiento']
    direccion=request.POST['direccion']
    ubigeo=request.POST['ubigeo']
    
    oEstablecimiento=Establecimiento.objects.get(id=id)   

    oEstablecimiento.tipo_establecimiento=tipo_establecimiento
    oEstablecimiento.ubigeo=ubigeo
    oEstablecimiento.direccion=direccion
    oEstablecimiento.usuario=oUsuario
    oEstablecimiento.save()

    return render(request,'establecimiento/index.html')

@csrf_exempt
def delete(request):
    id=request.POST['id']
    oEstablecimiento=Establecimiento.objects.get(id=id)
    oEstablecimiento.delete()
    return render(request,'establecimiento/index.html')