from rest_framework.permissions import BasePermission
from .models import Tour


class IsAdminUser(BasePermission):
    """Custom permission class to allow only admin users to create a tour."""

    def has_permission(self, request, view):
        print(request.user)
        return request.user.is_superuser


    