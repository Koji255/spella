from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.urls import reverse

from django.views.generic import ListView

from users.models import User

from speller_app.forms import TextInputForm
from speller_app.models import Report

from libs.text_handler.src.methods import speller



# Index
def index(request):
    return render(request, "speller_app/index.html")


# Text spell page
def spell(request):
    if request.method == "POST":
        form = TextInputForm(data=request.POST)
        
        if form.is_valid():
            text = str(form.cleaned_data["text"])

            spelled_text = speller(text)["spelled_text"]

            header = f"{spelled_text[:46]}..." if len(spelled_text) > 45 else spelled_text

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


# Particular page with spelled text from history page
def report(request, report_id):
    if request.user.is_authenticated:
        # Need to save in db spelled text
        spelled_text = Report.objects.get(pk=report_id).text

        return render(request, "speller_app/report.html", context={"spelled_text": spelled_text})

    return redirect(reverse("speller_app:index"))


# Spelled text history page
class HistoryView(LoginRequiredMixin, ListView):
    template_name = "speller_app/history.html"

    context_object_name = "object_list"

    def queryset(self):
        return Report.objects.filter(user_id=self.request.user.pk).order_by("-date").values_list("id", "header", "date")