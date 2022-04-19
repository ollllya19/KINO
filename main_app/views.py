from email import message
import re
from warnings import catch_warnings
from django.shortcuts import render
from .models import FilmLookUp, User, Film, FilmPurchase

genres = ['Drama', 'Action', 'Crime', 'Western','Adventure','Animation',
        'Biography', 'History', 'Romance', 'Fantasy', 'Comedy', 'Thriller', 'War', 'Mystery', 'Music']
genres.sort()


def signup(request):
    if request.method == "POST":
        if request.POST['login']=="" or request.POST['password']=="":
            return render(request, "main_app/IKINOREG.html")
        else:
            try:
                new_user = User.objects.create(phone=request.POST['login'], password=request.POST['password'])
                new_user.save()
                message = ""
            except:
                message = "Пользователь уже существует"
            return render(request, "main_app/IKINOREG.html", {'message' : message})  
    return render(request, "main_app/IKINOREG.html")


def signin(request):
    if request.method == "POST":
        try:
            userId  = User.objects.get(phone=request.POST['login'], password=request.POST['password']).id
            looked_films, paid_films = get_library(userId)
        except:
            message="Неправильный логин или пароль"
            return render(request, "main_app/IKINOINPUT.html", {'message': message})
        content = {'genres' : genres, 'user_id' : userId, 'genre': "Action", 'paid_films': paid_films,'looked_films': looked_films}
        return render(request, "main_app/lib.html", content)
    return render(request, "main_app/IKINOINPUT.html")


def search(request, user_id):
    title = request.GET['title']
    if title != '':
        found_films = filter_title(Film.objects.all(), title)
    else:
        found_films = Film.objects.all()
    looked_films, paidList = get_library(userId=user_id)
    content = {'genres' : genres, 'films': found_films, 'genre':"Action", "user_id": user_id, 'paid_list': paidList}
    return render(request, "main_app/ind.html", content)

def show_genre(request, genre, user_id):
    films, paidList = filter_genre(Film.objects.all()[:100], genre, user_id)
    looked_films, paidList = get_library(userId=user_id)
    content = {'genres' : genres, 'films': films, 'genre':genre, "user_id": user_id, 'paid_list': paidList}
    return render(request, "main_app/ind.html", content)

def library(request, user_id):
    looked_films, paid_films = get_library(userId=user_id)
    content = {'genres' : genres, 'paid_films': paid_films,'looked_films': looked_films, 'user_id': user_id, 'genre': 'Action'}
    return render(request, "main_app/lib.html", content)


def buy(request, genre = "Action", user_id = 0, film_id = 1):
    lookup = FilmLookUp.objects.create(userID=User.objects.get(id=user_id), filmID = Film.objects.get(id=film_id))
    lookup.save()
    content = {'genres': genres, 'user_id': user_id, 'film': Film.objects.get(id=film_id)}
    return render(request, "main_app/buy.html", content)

def pay(request, user_id, film_id):
    content = {'genres': genres, 'user_id': user_id, 'film': Film.objects.get(id=film_id)}
    new_buy = FilmPurchase.objects.create(userID=User.objects.get(id=user_id), filmID = Film.objects.get(id=film_id))
    new_buy.save()
    return render(request, "main_app/paid.html", content)


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



def filter_genre(films, req, user_id):
    rez = []
    boughtList = {}
    for obj in films:
        if req in obj.genre: 
            rez.append(obj)
            try:
                user = FilmPurchase(userID=user_id, filmID = obj.id)
                boughtList[obj.id] = True
            except:
                boughtList[obj.id] = False
    return rez, boughtList


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

def filter_looked_films(user):
    p = FilmLookUp.objects.filter(userID=user).order_by('datetime')
    rez = []
    for obj in p:
        rez.append(Film.objects.get(id=obj.filmID.id))
    return rez

def get_library(userId):
    paid_films = filter_purchase(userId)
    looked_films = set(filter_looked_films(userId)) - set(paid_films)
    return looked_films, paid_films