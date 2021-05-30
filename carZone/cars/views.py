from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_list = Car.objects.values_list('model', flat='True').distinct()
    city_list = Car.objects.values_list('city', flat='True').distinct()
    year_list = Car.objects.values_list('year', flat='True').distinct().order_by('-year')
    body_style_list = Car.objects.values_list('body_style', flat='True').distinct()

    data = {
        'cars': paged_cars,
        'model_list': model_list,
        'city_list': city_list,
        'year_list': year_list,
        'body_style_list': body_style_list,
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

    model_list = Car.objects.values_list('model', flat='True').distinct()
    city_list = Car.objects.values_list('city', flat='True').distinct()
    year_list = Car.objects.values_list('year', flat='True').distinct().order_by('-year')
    body_style_list = Car.objects.values_list('body_style', flat='True').distinct()
    transmission_list = Car.objects.values_list('transmission', flat='True').distinct()

    if 'Keyword' in request.GET:
        keyword = request.GET['Keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(description__icontains=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(description__icontains=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(description__icontains=year)

    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            cars = cars.filter(description__icontains=body_type)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_list': model_list,
        'city_list': city_list,
        'year_list': year_list,
        'body_style_list': body_style_list,
        'transmission_list': transmission_list,
    }
    return render(request, 'cars/search.html', data)
