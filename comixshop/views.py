from django.shortcuts import render, redirect


def main(request):
    list = [i for i in range(50)]
    return render(request, 'main.html', {'list':list})


def admin(request):
    return render(request, 'admin.html')