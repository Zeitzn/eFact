from django.urls import path

from apps.main import views

app_name='main'
urlpatterns = [
    path('', views.index, name='index'),
    # path('legalidad', views.legalidad, name='legalidad'),
    # path('quienessomos', views.quienes_somos, name='quienes_somos'),
    # path('testimonios', views.testimonios, name='testimonios'),
    # path('edfinanciera', views.ed_financiera, name='ed_financiera'),
    # path('contactenos', views.contactenos, name='contactenos'),
    # path('accounts/login/', views.index, name='account'),



]
