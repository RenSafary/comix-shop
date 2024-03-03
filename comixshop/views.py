from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.db.models import Q

from .models import *
from .forms import LoginForm, ImageForm


class Main(View):
    def post(self, request):
        # after the request
        admin = None
        if request.user.is_authenticated:
            admin = request.user.username
        
        # не доработан масштабный поиск
        if request.method == "POST":
            title = request.POST['find']

            title = title.lower()
            title = title[0].upper() + title[1:]
            try:
                books = Books.objects.filter(title=title)
            except:
                books = None

        return render(request, 'main/main.html', 
        {'books': books,
        'admin': admin})

    def get(self, request):
        # before the request
        books = Books.objects.all()

        admin = None
        if request.user.is_authenticated:
            admin = request.user.username
        return render(request, 'main/main.html', 
        {'books': books,
        'admin': admin})


def auth(request):
    if request.user.is_authenticated:
        return redirect("/products/")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username=cd['username'], password=cd['password'])

                if user is not None: # user.is_active() не нужно ура
                    login(request, user)
                    return redirect("/books/") # не работает, если нажать ещё, выдает incorrect csrf token
                else:
                    return JsonResponse({"message":"fail"})
            else:
                return HttpResponse("Form isn't valid")
        else:
            form = LoginForm()
    return render(request, 'admin-panel/auth.html', {'form': form})


def logout_(request):
    logout(request)
    return redirect("/")


class Book(View):
    def get(self, request):
        if request.user.is_authenticated:
            admin = request.user.username
            admin = admin[-1]

            type = None
            if admin == "1": type = "Манга"
            if admin == "2": type = "Манхва"
            if admin == "3": type = "Маньхуа"

            books = Books.objects.filter(type=type)
        else: 
            return redirect("/auth/")
        return render(request, 'admin-panel/books.html', {'books': books})
    
    def post(self, request):
        if request.method == "POST":
            operation = request.POST.get('operation')
            if operation == "Изменить":
                # edit
                title = request.POST['title']
                volume = request.POST['volume']
                description = request.POST['description']
                pages = request.POST['pages']
                amount = request.POST['amount']
                genre = request.POST['genre']

                print(title, volume, description, pages, amount, genre)
                books = Books.objects.filter(Q(title=title) | Q(volume=volume) | Q(description=description) | Q(pages=pages) | Q(amount=amount) | Q(genre=genre))    
                books.update(title=title, volume=volume, description=description, pages=pages, amount=amount, genre=genre)          
            else: 
                # delete
                id_book = request.POST['id_book']
                Books.objects.filter(id=id_book).delete()
        return redirect("/books/")
    

def add(request):
    if request.user.is_authenticated:
        admin = request.user.username
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                book = form.save(commit=False)
                if admin[-1] == "1": book.type = "Манга"
                elif admin[-1] == "2": book.type = "Манхва"
                elif admin[-1] == "3": book.type = "Маньхуа"
                book.save()
                return redirect('/books/add/')
            else:
                return HttpResponse("false")
        else:
            form = ImageForm()
    else:
        return redirect("/auth/")
    return render(request, 'admin-panel/add.html', {'form': form})