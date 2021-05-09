from django.urls import path, include
from cars import views
urlpatterns = [
    path('', views.cars, name='cars'),
]
