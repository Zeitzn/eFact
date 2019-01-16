from django.urls import path

from apps.producto import views

app_name='producto'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
