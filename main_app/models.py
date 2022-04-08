from distutils.command.build import build
from operator import truediv
from pyexpat import model
from tabnanny import verbose
from tkinter.tix import Tree
from django.db import models
from django.forms import model_to_dict


class User(models.Model):
    phone = models.CharField(max_length=64, unique=True, null=True)
    password = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"id: {self.id} Логин: {self.phone}  Пароль: {self.password}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Film(models.Model):
    photo = models.URLField(max_length=150, null = True)
    title = models.CharField(max_length=150, null = True)
    year = models.IntegerField(null = True)
    certificate = models.CharField(max_length=64, null = True, blank=True)
    runtime =  models.CharField(max_length=64, null = True)
    genre = models.CharField(max_length=64, null = True)
    rating = models.FloatField(null = True)
    overview = models.TextField(null = True)
    director = models.CharField(max_length=50, null = True)

    def __str__(self):
        return f"Название: {self.title}, жанр: {self.genre}, фото: {self.photo}, ревью: {self.overview}"

    class Meta:
            verbose_name = "Фильм"
            verbose_name_plural = "Фильмы"
            ordering = ['title']


class FilmPurchase(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    filmID = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True, auto_now=True)   
    cheque = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.userID}: {self.filmID}"

    class Meta:
            verbose_name = "Покупка"
            verbose_name_plural = "Покупки"
            ordering = ['date']