from rest_framework import serializers
from .models import Booking
from tours.models import Tour
from datetime import datetime
from pytz import timezone
import pytz
from django.core.exceptions import ValidationError

nairobi_time = timezone('Africa/Nairobi')

def get_available_tour_booking_slots(tour_booking_list,tour_capacity):
    total_current_bookings = 0
    for tour_booking in tour_booking_list:
        total_current_bookings += tour_booking.tickets
    available_slots = tour_capacity - total_current_bookings
    return available_slots

def can_make_booking(current_booking_tickets,available_slots):
    if available_slots <= 0 or available_slots < current_booking_tickets:
        return False
    return True

class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ( 
            'id','tickets', 
            'tour_id',)
        read_only_fields = ('updatedOn', 'createdOn')

    def validate(self, data):
        """
        Check that the date of booking is not on start date of tour or after the start .
        """
        
        if self.context['request'].method == 'POST':
            val_request = self.context['request'].data
            tour = Tour.objects.get(id=val_request['tour_id'])
            current_date = nairobi_time.localize(datetime.today())
            if tour.start_datetime <= current_date:
                raise serializers.ValidationError("The booking period for the tour has already past")
            tour_booking_list = Booking.objects.filter(tour_id=tour.id)
            available_slots = get_available_tour_booking_slots(tour_booking_list,tour.capacity)
            if not can_make_booking(val_request['tickets'], available_slots):
                booking_slots_error = "There are only {} tickets available for booking on this tour".format(
                    str(available_slots)
            )
                raise serializers.ValidationError(booking_slots_error)
        if self.context['request'].method == 'PUT' or self.context['request'].method == 'PATCH':
            val_request = self.context['request'].data
            context_view = self.context['view']
            if 'tickets' in val_request:
                tour_id = context_view.kwargs.get('pk', None)
                tour = Tour.objects.get(id=tour_id)
                current_date = nairobi_time.localize(datetime.today())
                if tour.start_datetime <= current_date:
                    raise serializers.ValidationError("The booking period for the tour has already past")
                tour_booking_list = Booking.objects.filter(tour_id=tour.id)
                available_slots = get_available_tour_booking_slots(tour_booking_list,tour.capacity)
                if not can_make_booking(val_request['tickets'], available_slots):
                    booking_slots_error = "There are only {} tickets available for booking on this tour".format(
                        str(available_slots)
                )
                    raise serializers.ValidationError(booking_slots_error)
                
        return data

    def create(self, validated_data):
        booking = Booking(**validated_data)
        booking_details = self.context['request'].data
        tour_id = booking_details['tour_id']
        try:
            tour = Tour.objects.get(id=tour_id)
        except Exception as e:
            raise serializer.ValidationError('The tour for this has been removed or does not exist')
        booking.tour_id = tour.id
        booking.pp_cost = tour.cost
        booking.createdBy_id = self.context['request'].user.id

        booking.save()
        return booking
