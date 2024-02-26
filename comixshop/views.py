from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import *
from .forms import LoginForm


def main(request):
    books = Book.objects.all()
    return render(request, 'main/main.html', 
    {'list':list,
    'books': books })


def auth(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None: # user.is_active() не нужно ура
                login(request, user)
                return redirect("/")
            else:
                return JsonResponse({"message":"fail"})
    else:
        form = LoginForm()
    return render(request, 'admin-panel/auth.html', {'form': form})


class Products(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'admin-panel/products.html', {'books': books})
    
    def post(self, request):
        # delete
        if request.method == "POST":
            id_book = request.POST['id_book']
            Book.objects.filter(id=id_book).delete()
        return redirect("/products/")