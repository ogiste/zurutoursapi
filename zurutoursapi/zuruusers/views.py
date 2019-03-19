from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserModelSerializer


# Create your views here.

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        serializer.save()