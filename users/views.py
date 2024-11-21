from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserRegistrationForm, UserLoginForm

from speller_app import views as speller_views
from . import views as users_views


# Create your views here.
def registration(request):
    """Registration view"""
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(users_views.login))
        
    else:
        form = UserRegistrationForm()
        
    context = {"form": form}

    return render(request, "users/registration.html", context)


def login(request):
    """Login view"""
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse(speller_views.index))
    
    else:
        form = UserLoginForm()

    context = {"form": form}
    
    return render(request, "users/login.html", context=context)