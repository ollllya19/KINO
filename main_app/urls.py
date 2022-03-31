from django.urls import path
from . import views

urlpatterns = [
    path("main_page/", views.main_page, name="main_page"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("films/", views.films, name="films")
]   