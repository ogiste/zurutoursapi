from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .permissions import IsAdminUser
from .models import Tour
from .serializers import TourModelSerializer



# Create your views here.

class TourCreate(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourModelSerializer
    permission_classes = (IsAdminUser,)
