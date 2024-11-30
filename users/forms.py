from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ("username", "email")


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("username", "password")


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",)