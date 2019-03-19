from django.test import TestCase
from .models import User

# Create your tests here.
class UserBaseTestCase(TestCase):
    """
    A class that defines the default user details variables used in the user model tests
    """
    def setUp(self):
        """
        A function that sets up the default user details variables used in the user model tests
        """
        self.test_user = {
            'username': 'test_username',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '254711999888',
            'email': 'testuser@gmail.com',
            'password': 'a123456',
        }

        self.test_user_fail = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'phone': '',
            'email': '',
            'password': '',
        }



