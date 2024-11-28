import re

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from users.models import User

from speller_app.forms import TextInputForm
from speller_app.models import Report

from libs.text_handler.src.methods import speller



# Create your views here.
def index(request):
    return render(request, "speller_app/index.html")


def spell(request):
    if request.method == "POST":
        form = TextInputForm(data=request.POST)
        
        if form.is_valid():
            text = str(form.cleaned_data["text"])

            spelled_text = speller(text)["spelled_text"]

            header = f"{spelled_text[:15]}..." if len(spelled_text) > 15 else spelled_text

            if request.user.is_authenticated:
            
                if report := Report.objects.create(
                    user=User.objects.get(pk=request.user.id), header=header, text=spelled_text):
                    
                    report.save()

            return render(request, "speller_app/speller.html", context={
                "form": form,
                "spelled_text": spelled_text,
                # Needs for dynamicaly changing of spelled text background area
                "lines": len(spelled_text) / 50,
            })
        
    else:
        form = TextInputForm()
    
    return render(request, "speller_app/speller.html", context={"form": form})