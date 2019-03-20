from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import TourCreate

urlpatterns = [
    path('', TourCreate.as_view(), name = 'create-tour'),
]