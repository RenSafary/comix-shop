from django.shortcuts import render, redirect
from .models import *


def main(request):
    books = Book.objects.all()
    return render(request, 'main.html', 
    {'list':list,
    'books': books })


def admin(request):
    return render(request, 'admin.html')