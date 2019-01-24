from django.urls import path

from apps.establecimiento import views
from django.contrib.auth.decorators import login_required

app_name='establecimiento'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('list', login_required(views.ListView.as_view()), name='list'),
    path('create', login_required(views.create), name='create'),
    path('update/<int:pk>', login_required(views.update), name='update'),
    path('delete/<int:pk>', login_required(views.delete), name='delete'),
]
