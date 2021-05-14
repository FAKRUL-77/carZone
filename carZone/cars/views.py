from django.shortcuts import render, get_object_or_404


# Create your views here.
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('created_date')

    data = {
        'cars': cars,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car_detail = get_object_or_404(Car, pk=id)
    data = {
        'single_car_detail': single_car_detail,
    }
    return render(request, 'cars/car_detail.html', data)
