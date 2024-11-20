from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserRegistrationForm

from speller_app import views


# Create your views here.
def registration(request):
    '''Registration view'''
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(views.index))
        
    else:
        form = UserRegistrationForm()
        
    context = {"form": form}

    return render(request, "users/registration.html", context)

