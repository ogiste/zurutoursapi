from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from zuruusers.views import UserCreate

urlpatterns = [
    path('users/', UserCreate.as_view(), name = 'create-user'), 
]