from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    ProfileForm
)



def login(request):
    if request.method == "POST":
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form=UserLoginForm()

    context={
        "title":"Логин",
        "form":form
    }
    return render(request, 'users/login.html',context)



def register(request):
    if request.method == "POST":
        form=UserRegistrationForm(data=request.POST, 
                                  files=request.FILES)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form=UserRegistrationForm()

    context={
        "title":"Регистрация",
        "form":form
    }
    return render(request, 'users/register.html',context)


def profile(request):
    if request.method == "POST":
        form=ProfileForm(data=request.POST, 
                        instance=request.user,
                        files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form=ProfileForm(instance=request.user)

    context={
        "title":"Профиль",
        "form":form

    }
    return render(request, 'users/profile.html',context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))
