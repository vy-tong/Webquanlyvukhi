from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from vktbapp.models import *
from django.contrib import messages
# Create your views here.


def viewpage(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    context={'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'base.html',context)

def loginpage(request): 
     if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')  # Chuyển hướng đến trang chính
        else:
            return render(request,"login.html",{'key':"Tên đăng nhập hoặc mật khẩu không chính xác!!!"})
     return render(request, "login.html")


def user_log(request):
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    context={'user_not_login':user_not_login, 'user_login':user_login}
    return render(request,context)





   


@login_required(login_url="login")

def vukhipage(request):   
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    Bienches = BienCheVuKhi.objects.all()
    context = {'user_not_login':user_not_login, 'user_login':user_login, "Bienches":Bienches}
    return render(request, "vukhi.html", context)

def trangbipage(request):   
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    Bienches = BienCheTrangBi.objects.all()
    context = {'user_not_login':user_not_login, 'user_login':user_login, "Bienches":Bienches}
    return render(request, "trangbi.html", context)

def logout_func(request):
    logout(request) 
    return HttpResponseRedirect('/')

# def vukhipage(request):
#    return render(request, 'vukhi.html')

def homepage(request):
    # return HttpResponse("Hello")
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    context={'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'home.html', context)

def aboutpage(request):
   # return HttpResponse("About page.")
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "unset"
    else:
        user_not_login = "unset"
        user_login = "none"
    context={'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'about.html', context)