from django.shortcuts import render
# from users.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    context={
        "title":"Логин",

    }
    return render(request, 'users/login.html',context)



def register(request):
    context={
        "title":"Регистрация",

    }
    return render(request, 'users/register.html',context)


def profile(request):
    context={
        "title":"Профиль",

    }
    return render(request, 'users/profile.html',context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
