from django.urls import path

from . import views

app_name = "speller_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("spell-the-text", views.spell, name="spell"),
    path("history", views.HistoryView.as_view(), name="history"),
    path("history/<int:report_id>", views.report, name="report"),
]