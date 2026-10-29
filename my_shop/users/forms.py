from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    
    )

from users.models import User



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    class Meta:
        model=User
        fields=(
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        )

# class UserProfileForm(ProfileForm):
#     pass
