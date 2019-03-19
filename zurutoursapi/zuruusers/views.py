from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import User
from .serializers import UserModelSerializer



# Create your views here.

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (permissions.AllowAny,)
    def perform_create(self, serializer):
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (permissions.IsAuthenticated,)