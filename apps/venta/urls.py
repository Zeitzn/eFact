from django.urls import path

from apps.venta import views
from django.contrib.auth.decorators import login_required
app_name='venta'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('gen/', login_required(views.generarVenta), name='generar'),
    path('registrar/', login_required(views.registrarFactura), name='registrarFactura'),
]
