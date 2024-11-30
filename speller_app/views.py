import datetime

from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Min

from django.http import HttpResponse

from django.urls import reverse

from django.views.generic import ListView

from users.models import User

from speller_app.forms import TextInputForm
from speller_app.models import Report

from libs.text_handler.src.methods import speller



def index(request):
    return render(request, "speller_app/index.html")


def spell(request):
    '''View with main functionality of this web application'''
    # For the 'POST' case
    if request.method == "POST":
        form = TextInputForm(data=request.POST)
        
        if form.is_valid():
            text = str(form.cleaned_data["text"])
            # Using outer text_handler library to spell user's input
            spelled_text = speller(text)["spelled_text"]
            # Header for report row in db
            header = f"{spelled_text[:46]}..." if len(spelled_text) > 45 else spelled_text
            # Reports storing logic
            if request.user.is_authenticated:
                # Taking a user
                user = User.objects.get(pk=request.user.id)
                # DB stores only 15 reports for user. Than it starts to update old ones
                if len(Report.objects.filter(user=user).all()) < 15:
                    report = Report.objects.create(user=user, header=header, text=spelled_text)

                    report.save()

                else:
                    # Finds oldest report
                    oldest_report = Report.objects.filter(user=user).aggregate(Min("date"))
                    # Pops oldest one
                    report = Report.objects.filter(user=user, date=oldest_report["date__min"]).update(
                        header=header, text=spelled_text, date=datetime.datetime.today())

            return render(request, "speller_app/speller.html", context={
                "form": form,
                "spelled_text": spelled_text,
                # Needs for dynamicaly changing of spelled text background area
                "lines": len(spelled_text) / 50,
            })
    # For 'GET' scenario 
    else:
        form = TextInputForm()

    return render(request, "speller_app/speller.html", context={"form": form})


def report(request, report_id):
    '''View with stored in the db user's spelled output'''
    # User's session validation
    if request.user.is_authenticated:
        spelled_text = Report.objects.get(pk=report_id).text

        return render(request, "speller_app/report.html", context={"spelled_text": spelled_text})

    return redirect(reverse("speller_app:index"))


class HistoryView(LoginRequiredMixin, ListView):
    '''View with table of spells history'''
    template_name = "speller_app/history.html"

    context_object_name = "object_list"

    def queryset(self):
        return Report.objects.filter(user_id=self.request.user.pk).order_by("-date").values_list("id", "header", "date")