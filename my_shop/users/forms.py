from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm
    
    )

from users.models import User



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

class UserRegistrationForm(UserCreationForm):
    image=forms.ImageField(required=False)
    first_name=forms.CharField()
    # last_name=forms.CharField()
    username=forms.CharField()
    number=forms.CharField(max_length=12)
    email=forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model=User
        fields=(
            "image",
            "first_name",
            # "last_name",
            "username",
            "number",
            "email",
            "password1",
            "password2"
        )

class ProfileForm(UserChangeForm):
    image=forms.ImageField(required=False)
    first_name=forms.CharField()
    # last_name=forms.CharField()
    number=forms.CharField(max_length=12)
    username=forms.CharField()
    email=forms.EmailField()

    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            # "last_name",
            "number",
            "username",
            "email"
        )
