from django.urls import path

from apps.cliente import views
from django.contrib.auth.decorators import login_required

app_name='cliente'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    
]
