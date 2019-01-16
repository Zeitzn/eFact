from django.urls import path

from apps.producto import views
from django.contrib.auth.decorators import login_required
app_name='producto'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('update/', login_required(views.update), name='update'),
    path('delete/', login_required(views.delete), name='delete'),
]
