from django.contrib import admin

from .models import FilmLookUp, User, Film, FilmPurchase

admin.site.register(User)
admin.site.register(Film)
admin.site.register(FilmPurchase)
admin.site.register(FilmLookUp)