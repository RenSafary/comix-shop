from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from .models import *
from .forms import LoginForm


def main(request):
    books = Book.objects.all()
    return render(request, 'main/main.html', 
    {'list':list,
    'books': books })


def admin(request):
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