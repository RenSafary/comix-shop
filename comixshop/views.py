from django.shortcuts import render, redirect
from .models import *


def main(request):
    book = Book.objects.all()
    return render(request, 'main.html', 
    {'list':list,
    'book': book })


def admin(request):
    return render(request, 'admin.html')