from django.test import TestCase
from .user_base_test import UserBaseTestCase
from .models import User
from rest_framework.test import APIClient
from django.urls import path, reverse
from rest_framework import status

# Create your tests here.
class UserModelTestCase(UserBaseTestCase):
    def test_user_can_register(self):
        """
        Test to assert if User Model can create a new user successfully.
        """

        self.users = User(**self.test_user)
        self.users.save()
        users = User.objects.all()
        self.assertEqual(len(users), 1)


class UserViewTestCase(UserBaseTestCase):
    def setUp(self):
        """
        Sets up client api for testing posting users in the model.
        """
        self.test_user = {
            'username': 'test_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a123456',
        }
        self.client = APIClient()
        

    def test_api_can_create_user(self):
        """
        Test to assert if API creates user successfully
        """
        response = self.client.post(
            reverse('create-user'),
            self.test_user,
            format = 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_a_user(self):
        """Test the api can get a given user."""
        user = User.objects.get()
        response = self.client.get(
            reverse('user-details',
            kwargs={'pk': user.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    def test_api_can_update_user(self):
        """Test the api can update a given user."""
        change_last_name = {'last_name': 'Fakename'}
        res = self.client.put(
            reverse('user-details', kwargs={'pk': user.id}),
            change_last_name, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_user(self):
        """Test the api can delete a user."""
        user = User.objects.get()
        response = self.client.delete(
            reverse('user-details', kwargs={'pk': user.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


        

    

    



