from django.contrib import admin

from .models import User, Film, FilmPurchase

admin.site.register(User)
admin.site.register(Film)
admin.site.register(FilmPurchase)