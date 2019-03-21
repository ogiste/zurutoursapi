from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUser, CanGetOrCreateBooking, CanReadUpdateDeleteSingleBooking
from rest_framework.permissions import AllowAny
from .models import Booking
from .serializers import BookingModelSerializer

class BookingListCreate(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = (CanGetOrCreateBooking,)

class BookingDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = (CanReadUpdateDeleteSingleBooking,)