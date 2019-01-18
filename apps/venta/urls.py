from django.urls import path

from apps.venta import views
from django.contrib.auth.decorators import login_required
app_name='venta'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('gen/', login_required(views.generate), name='generar'),
    # path('delete/', login_required(views.delete), name='delete'),
]
