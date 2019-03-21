from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """ 
    This class represents the User model

    A user has:
    username: Unique string of characters used to identify the user ,
    first_name: String of characters used to store a user's first name,
    last_name: String of characters used to store a user's second name,
    phone: String of characters used to store a user's phone number,
    email: String of characters used to store a user's email,
    password: String of characters used to store a users password,
    updatedOn: DateTime for last user details update,

    """
    phone = models.CharField( max_length=12, default="254777777777", blank=False)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human readable representation of the user instance.
        """
        return "id:{}, username: {}, first_name:{}, last_name:{}, phone:{}, is_superuser:{}, is_staff:{} ".format(
            self.id,
            self.username,
            self.first_name,
            self.last_name,
            self.phone,
            self.is_superuser,
            self.is_staff,
            )
    


