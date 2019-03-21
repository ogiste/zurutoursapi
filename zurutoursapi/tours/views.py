from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUser, CanGetOrCreateTour, CanReadUpdateDeleteSingleTour
from rest_framework.permissions import AllowAny
from .models import Tour
from .serializers import TourModelSerializer



# Create your views here.

class TourListCreate(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourModelSerializer
    permission_classes = (CanGetOrCreateTour,)

class TourDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourModelSerializer
    permission_classes = (CanReadUpdateDeleteSingleTour,)
