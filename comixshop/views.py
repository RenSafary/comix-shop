from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import *
from .forms import LoginForm, ImageForm


class Main(View):
    def post(self, request):
        admin = None
        if request.user.is_authenticated:
            admin = request.user.username
        
        if request.method == "POST":
            title = request.POST['find']

            title = title.lower()
            re_title = ""
            for i in title:
                if i != " " or i != ":" or i != "-" or i != "." or i != ",":
                    re_title = re_title + i
            re_title = re_title[0].upper() + re_title[1:]
            try:
                books = Books.objects.filter(title=re_title)
            except:
                books = None

        return render(request, 'main/main.html', 
        {'books': books,
        'admin': admin})

    def get(self, request):
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
                    return redirect("/products/") # не работает, если нажать ещё, выдает incorrect csrf token
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


class Products(View):
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
        return render(request, 'admin-panel/products.html', {'books': books})
    
    def post(self, request):
        if request.method == "POST":
            operation = request.POST.get('operation')
            if operation == "Изменить":
                # edit
                old_title = request.POST['old title']
                title = request.POST['title']
                type = request.POST['type']
                description = request.POST['description']
                pages = request.POST['pages']
                amount = request.POST['amount']
                #genre = request.POST['genre']

                Books.objects.filter(title=old_title).update(title=title,
                type=type, description=description, pages=pages, amount=amount)              
            else: 
                # delete
                id_book = request.POST['id_book']
                Books.objects.filter(id=id_book).delete()
        return redirect("/products/")
    

def add(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/add/')
        else:
            return HttpResponse("false")
    else:
        form = ImageForm()
    return render(request, 'admin-panel/add.html', {'form': form})