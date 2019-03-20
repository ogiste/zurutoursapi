from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import TourListCreate

urlpatterns = [
    path('', TourListCreate.as_view(), name = 'create-tour'),
]