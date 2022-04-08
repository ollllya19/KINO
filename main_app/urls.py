from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("films/<int:login_id>", views.films, name="films"),
    path("films/<str:genre>", views.show_genre, name="show_genre"),
    path("films/library/<int:user_id>", views.pers_library, name="pers_library"),
    path("films/<int:user_id>", views.pers_library, name="pers_library"),
]   