from django.shortcuts import render


def home(request, name):
    context = {"name": name}
    return render(request, 'menu/home.html', context)