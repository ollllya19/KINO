import re
from warnings import catch_warnings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User, Film, FilmPurchase

genres = ['Drama', 'Action', 'Crime', 'Western','Adventure','Animation',
        'Biography', 'History', 'Romance', 'Fantasy', 'Comedy', 'Thriller', 'War', 'Mystery', 'Music']
genres.sort()


def main_page(request):
    return render(request, "main_app/main_page.html")


def signup(request):
    if request.method == "POST":
        if request.POST['login']=="" or request.POST['password']=="":
            return render(request, "main_app/IKINOREG.html")
        else:
            new_user = User.objects.create(phone=request.POST['login'], password=request.POST['password'])
            new_user.save()
            return render(request, "main_app/IKINOINPUT.html")  
    return render(request, "main_app/IKINOREG.html")


def signin(request):
    if request.method == "POST":
        user = User.objects.get(phone=request.POST['login'], password=request.POST['password'])
        films = filter_purchase(user.id)
        content = {'genres' : genres, 'films': films, 'user_id' : user.id}
        return render(request, "main_app/lib.html", content)
    return render(request, "main_app/IKINOINPUT.html")



def films(request, login_id):
    films = filter_purchase(28)
    content = {'genres' : genres, 'films': films}
    return render(request, "main_app/ind.html", content)

def show_genre(request, genre):
    films = filter_genre(Film.objects.all(), genre)
    content = {'genres' : genres, 'films': films}

    return render(request, "main_app/ind.html", content)

def pers_library(request, user_id):
    films = filter_purchase(user_id)
    content = {'genres' : genres, 'films': films, 'user_id': user_id}

    return render(request, "main_app/lib.html", content)


def buying(request, user_id, film_id):
    new_buy = FilmPurchase.objects.create(userID=user_id, filmID = film_id)
    content = {'films' : films, 'genres': genres, 'user_id': user_id}
    return render(request, "main_app/buy.html", content)


def user(request, login_id):
    years = set(list(map(lambda t: t.year, Film.objects.order_by('year'))))
    
    if request.method == 'POST':
        films_on_title = set(Film.objects.all())
        films_on_year = set(Film.objects.all())
        films_on_genre = set(Film.objects.all())

        if request.POST['title'] != '':
            films_on_title =  set(filter_title(Film.objects.all(), request.POST['title']))
        if request.POST['year_value'] != '':
            films_on_year = set(filter_year(Film.objects.all(), int(request.POST['year_value'])))
        if request.POST['genre'] != '':
            films_on_genre = set(filter_genre(Film.objects.all(), request.POST['genre']))
        films = films_on_title & films_on_genre & films_on_year
    else:
        films = filter_purchase(login_id)

    content = {'films' : films, 'genres': genres, 'years': years, 'user_id': login_id}
    return render(request, "main_app/films.html", content)

# filter films on genre
def filter_genre(films, req):
    rez = []
    for obj in films:
        if req in obj.genre: rez.append(obj)
    return rez

def filter_title(films, req):
    rez = []
    for obj in films:
        if req in obj.title: rez.append(obj)
    return rez

def filter_year(films, req):
    rez = []
    for obj in films:
        if req == obj.year: rez.append(obj)
    return rez

def filter_purchase(user):
    p = FilmPurchase.objects.filter(userID=user)
    rez = []
    for obj in p:
        rez.append(Film.objects.get(id=obj.filmID.id))
    return rez