from django.test import TestCase
from zuruusers.models import User
from .models import Booking
from rest_framework.test import APIClient
from django.urls import path, reverse
from rest_framework import status
from datetime import date, datetime, timedelta
from pytz import timezone
import pytz
from rest_framework_simplejwt.tokens import RefreshToken
from zuruusers.models import User
from tours.models import Tour

nairobi_time = timezone('Africa/Nairobi')
class BookingModelTest(TestCase):
    def test_booking_can_be_created(self):
        """
        Test to assert if Booking Model can create a new booking successfully.
        """
        self.client = APIClient()

        # Create a  normal user as a test user for creating a booking
        self.test_user = {
            'username': 'test_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a1234567',
        }
        self.users = User(**self.test_user)
        self.users.save()
        self.auth_user = User.objects.get()

        # Create an admin user to create a tour
        self.test_admin_user = {
            'username': 'test_admin_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a123456',
        }
        self.new_admin_user = User(**self.test_admin_user)
        self.new_admin_user.is_superuser = True
        self.new_admin_user.is_staff = True
        self.new_admin_user.save()
        
        # Create the tour with the administrator
        tokens = RefreshToken.for_user(self.new_admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        
        current_date = nairobi_time.localize(datetime.today())
        start_date = datetime.today() + timedelta(days=6) 
        start_date = start_date.isoformat(' ')
        end_date = datetime.fromisoformat(start_date) + timedelta(days=2)
        
        self.test_tour = {
            'title': 'Test Tour',
            'cost': 5000.00,
            'capacity': 20,
            'start_datetime': start_date,
            'end_datetime': end_date,
            'description': 'First description',
        }

        response = self.client.post(
            reverse('create-tour'),
            self.test_tour,
            format = 'json'
        )
        self.tour = Tour.objects.get()
        self.client.credentials()

        # Create the booking with the normal user
        tokens = RefreshToken.for_user(self.auth_user)
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        self.test_booking = {
            'tour_id': self.tour.id,
            'tickets': 5,
            'pp_cost': 5000.00,
            'createdBy_id': self.auth_user.id,
        }
        
        self.bookings = Booking(**self.test_booking)
        self.bookings.save()
        bookings = Booking.objects.all()
        self.assertEqual(len(bookings), 1)

class BookingViewTestCase(TestCase):
    def setUp(self):
        """
        Setup Tour Tests for Booking views
        """
        self.client = APIClient()

        # Create a  normal user as a test user for creating a booking
        self.test_user = {
            'username': 'test_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a1234567',
        }
        self.users = User(**self.test_user)
        self.users.save()
        self.auth_user = User.objects.get()

        # Create an admin user to create a tour
        self.test_admin_user = {
            'username': 'test_admin_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a123456',
        }
        self.new_admin_user = User(**self.test_admin_user)
        self.new_admin_user.is_superuser = True
        self.new_admin_user.is_staff = True
        self.new_admin_user.save()
        
        # Create the tour with the administrator
        tokens = RefreshToken.for_user(self.new_admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        current_date = nairobi_time.localize(datetime.today())
        start_date = datetime.today() + timedelta(days=6) 
        start_date = start_date.isoformat(' ')
        end_date = datetime.fromisoformat(start_date) + timedelta(days=2)
        
        self.test_tour = {
            'title': 'Test Tour',
            'cost': 5000.00,
            'capacity': 20,
            'start_datetime': start_date,
            'end_datetime': end_date,
            'description': 'First description',
        }

        response = self.client.post(
            reverse('create-tour'),
            self.test_tour,
            format = 'json'
        )
        self.tour = Tour.objects.get()
        self.client.credentials()

        # Create the booking with the normal user
        tokens = RefreshToken.for_user(self.auth_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        self.test_booking = {
            'tour_id': self.tour.id,
            'tickets': 1,
            'pp_cost': 5000.00,
            'createdBy_id': self.auth_user.id,

        }
        self.bookings = Booking(**self.test_booking)
        self.bookings.save()

    def test_tour_view_can_create_booking(self):
        """
        Test to assert if API creates bookings successfully
        """
        response = self.client.post(
            reverse('createlist-booking'),
            self.test_booking,
            format = 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_tour_view_can_list_bookings(self):
        """
        Test to assert if API list all bookings successfully if user is an admin
        """
        self.client.credentials()
        tokens = RefreshToken.for_user(self.new_admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        response = self.client.get(
            reverse('createlist-booking')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tour_view_can_retrieve_a_booking(self):
        """
        Test to assert if API retrieve a booking successfully if user is an admin or booking owner
        """
        response = self.client.get(
            reverse('details-booking',kwargs={'pk': self.bookings.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tour_view_can_update_bookings(self):
        """
        Test to assert if API can update a booking successfully if user is an admin
        """
        self.client.credentials()
        tokens = RefreshToken.for_user(self.new_admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        response = self.client.patch(
            reverse('details-booking', kwargs={'pk': self.bookings.id}),
            {'pp_cost': 4000.40},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tour_view_can_delete_booking(self):
        """
        Test to assert if API can delete a booking successfully if user is an admin or owner
        """
        response = self.client.delete(
            reverse('details-booking',kwargs={'pk': self.bookings.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

