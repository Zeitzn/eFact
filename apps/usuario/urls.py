from django.urls import path

from apps.usuario import views
from django.contrib.auth.decorators import login_required
app_name='usuario'
urlpatterns = [
    # path('', login_required(views.index), name='index'),   
    path('getUserSession', login_required(views.getUserSession), name='getUserSession'),
]
