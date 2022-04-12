from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("films/library/<int:user_id>/", views.library, name="pers_library"),
    path("films/pay/<int:user_id>/<int:film_id>/", views.pay, name="pay"),
    path("films/<str:genre>/<int:user_id>/", views.show_genre, name="show_genre"),
    path("films/<str:genre>/<int:user_id>/<int:film_id>/", views.buy, name="buy"),
]   