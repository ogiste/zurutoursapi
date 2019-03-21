from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from zuruusers.views import UserCreate, UserDetailsView

urlpatterns = [
    path('', UserCreate.as_view(), name = 'create-user'),
    path('<int:pk>/', UserDetailsView.as_view(), name = 'details-user'),
]