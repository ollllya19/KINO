import re
from warnings import catch_warnings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User, Film

def main_page(request):
    return render(request, "main_app/main_page.html")

#authorization
def signup(request):
    if request.method == "POST":
        if request.POST['name']=="" or request.POST['login']=="" or request.POST['password']=="":
            return render(request, "main_app/signup.html", {"message" : "Необходимо заполнить все поля"})
        else:
            new_user = User.objects.create(name=request.POST['name'], login=request.POST['login'], password=request.POST['password'])
            new_user.save()
            return render(request, "main_app/signin.html")
    else:
        return render(request, "main_app/signup.html", {"message" : ""})


#registration
def signin(request):
    try:
        u1 = User.objects.filter(login=request.GET['login'])
        u2 = u1.exclude(password=request.GET['password'])
    except:
        return render(request, "main_app/signin.html")


def films(request):
    genres = ['Все жанры','Drama', 'Action', 'Crime', 'Western','Adveture','Animation']
    years = set(list(map(lambda t: t.year, Film.objects.order_by('year'))))
    if request.method == 'POST':
        films_on_year = Film.objects.filter(year=int(request.POST['year_value']))
        films = get_film_on_genre(films_on_year, request.POST['genre'])
    else:
        films = Film.objects.all()

    return render(request, "main_app/films.html", {'films' : films, 
                                                   'genres': genres,
                                                   'years': years})

def get_film_on_genre(films, req):
    rez = []
    for obj in films:
        if req in obj.genre: rez.append(obj)
    return rez