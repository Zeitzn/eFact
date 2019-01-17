from django.urls import path

from apps.establecimiento import views
from django.contrib.auth.decorators import login_required

app_name='establecimiento'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
