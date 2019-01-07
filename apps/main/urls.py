from django.urls import path

from apps.main import views

app_name='main'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    # path('testimonios', views.testimonios, name='testimonios'),
    # path('edfinanciera', views.ed_financiera, name='ed_financiera'),
    # path('contactenos', views.contactenos, name='contactenos'),
    # path('accounts/login/', views.index, name='account'),



]
