from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .permissions import IsAdminUser, CanGetOrCreateTour
from rest_framework.permissions import AllowAny
from .models import Tour
from .serializers import TourModelSerializer



# Create your views here.

class TourListCreate(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourModelSerializer
    permission_classes = (CanGetOrCreateTour,)
