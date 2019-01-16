from django.urls import path

from apps.establecimiento import views

app_name='establecimiento'
urlpatterns = [
    path('', views.index, name='index'),
    # path('update/', views.update, name='update'),
    # path('delete/', views.delete, name='delete'),
]
