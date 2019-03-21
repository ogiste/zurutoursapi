from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import BookingListCreate, BookingDetailsView

urlpatterns = [
    path('', BookingListCreate.as_view(), name = 'createlist-booking'),
    path('<int:pk>/', BookingDetailsView.as_view(), name = 'details-booking' )
]