from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')


def cars(request):
    return render(request, 'pages/cars.html')


def services(request):
    return render(request, 'pages/services.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')