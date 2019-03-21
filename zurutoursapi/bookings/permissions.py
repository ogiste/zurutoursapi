from rest_framework.permissions import BasePermission
from .models import Booking
from tours.models import Tour

def can_read_or_delete_booking(req_user, booking_id ):
    if(isinstance(booking_id, int)):
        booking_details = Booking.objects.get(pk=booking_id)
        if req_user.id == booking_details.createdBy_id or (req_user.is_admin or req_user.is_staff) :
            return True
    return False



class IsAdminUser(BasePermission):
    """Custom permission class to allow only admin users to create a Booking."""

    def has_permission(self, request, view):
        return (request.user.is_superuser or request.user.is_staff)

class CanGetOrCreateBooking(BasePermission):
    """Custom permission class to allow only authenticated users to create a booking and admin users to view all bookings."""

    def has_permission(self, request, view):
        if request.method == 'GET' and (request.user.is_superuser or request.user.is_staff):
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return False

class CanReadUpdateDeleteSingleBooking(BasePermission):
    def has_permission(self, request, view):
        booking_id = view.kwargs.get('pk', None)
        if (request.method == 'GET' and request.user.is_authenticated 
            and can_read_or_delete_booking(request.user, booking_id )) :
            return True
        if (request.method == 'UPDATE' and request.user.is_authenticated
            and (request.user.is_staff or request.user.is_admin)):
            return True
        if (request.method == 'DELETE' and request.user.is_authenticated 
            and can_read_or_delete_booking(request.user, booking_id)):
            return True
        return (request.user.is_superuser or request.user.is_staff) and request.user.is_authenticated
    