from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'main/index.html')

def login_template(request):
    return render(request,'main/login.html')

# @csrf_exempt
def login(request):    
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
        auth_login(request, usuario)
        return redirect('home:index')
    else:
        return redirect('main:login_template')

def register(request):
    return render(request,'main/register.html')
