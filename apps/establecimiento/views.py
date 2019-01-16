from django.shortcuts import render
from apps.establecimiento.models import Establecimiento
from apps.usuario.models import Usuario
from django.contrib import messages
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