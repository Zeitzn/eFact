from django.shortcuts import render
from django.http import HttpResponse
from apps.usuario.models import Usuario
from django.core import serializers

# Create your views here.

def getUserSession(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''
    
    usuario_id=oUsuario.id

    # data = serializers.serialize(
    #     'json',
    #     oUsuario,
    #     fields = ['id']
    # )
    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(str(usuario_id))