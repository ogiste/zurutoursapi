from rest_framework.permissions import BasePermission
from .models import User


class IsOwner(BasePermission):
    """Custom permission class to allow only user owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the user owner."""
        if isinstance(obj, User):
            return obj.owner == request.user
        return obj.owner == request.user