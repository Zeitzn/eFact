from django.urls import path

from apps.home import views
from django.contrib.auth.decorators import login_required
app_name='home'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    # path('legalidad', views.legalidad, name='legalidad'),
    # path('quienessomos', views.quienes_somos, name='quienes_somos'),
    # path('testimonios', views.testimonios, name='testimonios'),
    # path('edfinanciera', views.ed_financiera, name='ed_financiera'),
    # path('contactenos', views.contactenos, name='contactenos'),
    # path('accounts/login/', views.index, name='account'),



]
