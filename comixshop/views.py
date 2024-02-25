from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .models import *
from .forms import LoginForm


def main(request):
    books = Book.objects.all()
    return render(request, 'main.html', 
    {'list':list,
    'books': books })


def admin(request): # респонсы не приходят
    if request.method == "Post":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Вход выполнен.")
                else:
                    return HttpResponse("Ошибка входа.")
            else:
                return HttpResponse("Аккаунт не найден.")
    else:
        form = LoginForm()
    return render(request, 'admin.html', {'form': form})