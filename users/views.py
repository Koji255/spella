from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm

from speller_app import views as speller_views
from . import views as users_views


# Views here
def registration(request):
    """Registration view"""
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(users_views.login))
        
    else:
        form = UserRegistrationForm()

    return render(request, "users/registration.html", {"form": form})


def login(request):
    """Login view"""
    if request.method == "POST":
        post = request.POST
        # Audit
        form = UserLoginForm(data=post)

        if form.is_valid():
            # Authentication
            if user := auth.authenticate(username=post["username"], 
                                         password=post["password"]):
                # Authorisation
                auth.login(request, user)

                return HttpResponseRedirect(reverse(speller_views.index))
    
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", context={"form": form})


def logout(request):
    """Logout view"""
    auth.logout(request)

    return HttpResponseRedirect(reverse(speller_views.index))


def profile(request):
    """Profile view"""
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse(users_views.profile))
        
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "users/profile.html", {"form": form})