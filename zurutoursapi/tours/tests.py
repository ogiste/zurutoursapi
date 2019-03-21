from django.test import TestCase
from zuruusers.models import User
from .models import Tour
from rest_framework.test import APIClient
from django.urls import path, reverse
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from zuruusers.models import User

class TourModelTest(TestCase):
    def test_tour_can_be_created(self):
        """
        Test to assert if Tour Model can create a new tour successfully.
        """
        self.test_user = {
            'username': 'test_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a1234567',
        }
        User(**self.test_user)
        self.client = APIClient()
        
        self.response = self.client.post(
            reverse('create-user'),
            self.test_user,
            format = 'json'
        )
        self.auth_user = User.objects.get()
        self.client.force_authenticate(user=self.auth_user)
        current_date = datetime.today()
        start_date = current_date.isoformat(' ')
        end_date = datetime.fromisoformat(start_date) + timedelta(days=1)
        
        self.test_tour = {
            'title': 'Test Tour',
            'cost': 5000.00,
            'capacity': 20,
            'start_datetime': start_date,
            'end_datetime': end_date,
            'description': 'First description',
            'createdBy_id': self.auth_user.id,
        }

        self.tours = Tour(**self.test_tour)
        self.tours.save()
        tours = Tour.objects.all()
        self.assertEqual(len(tours), 1)
        



class TourViewTestCase(TestCase):
    def setUp(self):
        """
        Setup Tour Tests for tour views
        """
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
        self.client = APIClient()
        # self.auth_user = User.objects.get()
        tokens = RefreshToken.for_user(self.new_admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        # self.client.force_authenticate(user=self.new_admin_user)
        current_date = datetime.today()
        start_date = current_date.isoformat(' ')
        end_date = datetime.fromisoformat(start_date) + timedelta(days=1)
        
        self.test_tour = {
            'title': 'Test Tour',
            'cost': 5000.00,
            'capacity': 20,
            'start_datetime': start_date,
            'end_datetime': end_date,
            'description': 'First description',
        }

    def test_tour_view_can_create_tour(self):
        """
        Test to assert if API creates tour successfully
        """
        response = self.client.post(
            reverse('create-tour'),
            self.test_tour,
            format = 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

