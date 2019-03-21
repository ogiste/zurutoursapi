from django.db import models
from zuruusers.models import User
from tours.models import Tour

# Create your models here.
class Booking(models.Model):
    """ 
    This class represents the User model

    A booking has:
    createdBy_id = User id of the user by whom the booking was created
    updatedOn = DateTime the most recent booking update took place
    createdOn = DateTime the booking was created
    tickets =  Number of people booked in a single booking instance
    pp_cost = Cost per person for the booking
    tour_id = Tour for which the booking was made

    """
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedOn = models.DateTimeField("Updated On", auto_now=True)
    createdOn = models.DateTimeField("Created On", auto_now_add=True)
    tickets = models.IntegerField("Number of people booked", blank=False)
    pp_cost = models.DecimalField("Booking Cost Per Person", max_digits=7, decimal_places=2, blank=False)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human readable representation of the booking instance.
        """
        return "Tour object tickets: {},\n pp_cost:{},\n tour_id:{},\n createdOn:{},\n createdBy:{} ".format(
            self.tickets,
            self.pp_cost,
            self.tour,
            self.createdOn,
            self.createdBy,
            )