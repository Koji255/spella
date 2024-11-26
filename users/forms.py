from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("username", "password")


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",)