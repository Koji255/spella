from django.urls import path

from django.forms import BaseForm

from . import views

app_name = "speller_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("spell_the_text", views.spell, name="spell"),
]