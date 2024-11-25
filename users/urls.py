from django.urls import path

from . import views


urlpatterns = [
    path("register", views.registration, name="user_registration"),
    path("login", views.login, name="user_login"),
    path("profile", views.profile, name="user_profile"),
]