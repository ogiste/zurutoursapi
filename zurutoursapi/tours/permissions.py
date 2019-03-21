from rest_framework.permissions import BasePermission
from .models import Tour


class IsAdminUser(BasePermission):
    """Custom permission class to allow only admin users to create a tour."""

    def has_permission(self, request, view):
        return (request.user.is_superuser or request.user.is_staff)

class CanGetOrCreateTour(BasePermission):
    """Custom permission class to allow only admin users to create a tour and all users to view tours."""

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return (request.user.is_superuser or request.user.is_staff) and request.user.is_authenticated

class CanReadUpdateDeleteSingleTour(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return (request.user.is_superuser or request.user.is_staff) and request.user.is_authenticated
    