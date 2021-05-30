from django.shortcuts import render

# Create your views here.
from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('created_date')

    model_list = Car.objects.values_list('model', flat='True').distinct()
    city_list = Car.objects.values_list('city', flat='True').distinct()
    year_list = Car.objects.values_list('year', flat='True').distinct()
    body_style_list = Car.objects.values_list('body_style', flat='True').distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_list': model_list,
        'city_list': city_list,
        'year_list': year_list,
        'body_style_list': body_style_list,
    }

    return render(request, 'pages/home.html', data)


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
