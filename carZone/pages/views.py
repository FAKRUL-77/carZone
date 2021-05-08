from django.shortcuts import render

# Create your views here.
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)


def cars(request):
    return render(request, 'pages/cars.html')


def services(request):
    return render(request, 'pages/services.html')


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def contact(request):
    return render(request, 'pages/contact.html')