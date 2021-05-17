from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


# Create your views here.
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car_detail = get_object_or_404(Car, pk=id)
    data = {
        'single_car_detail': single_car_detail,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('created_date')

    if 'Keyword' in request.GET:
        keyword = request.GET['Keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    data = {
        'cars': cars,
    }
    return render(request, 'cars/search.html', data)
