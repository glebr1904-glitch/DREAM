from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import (
    UserLoginForm,
                         
    )



def login(request):
    if request.method == "POST":
        form=UserLoginForm(data=request.POST)
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
    return HttpResponseRedirect(reverse('main:index'))
