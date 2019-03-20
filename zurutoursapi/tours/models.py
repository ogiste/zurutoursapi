from django.db import models
from zuruusers.models import User

# Create your models here.
class Tour(models.Model):
    """ 
    This class represents the User model

    A tour has:
    createdBy = User id of the user by whom the tour was created
    updatedOn = DateTime the most recent tour update took place
    createdOn = DateTime the tour was created
    description = Description of the experience offered by the tour
    end_datetime = DateTime the tour is expected to end
    start_datetime = DateTime the tour is expected to start
    capacity = Maximum number of people that can book the tour
    cost = Cost per person for the tour
    title = Title of the tour

    """
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedOn = models.DateTimeField("Updated On", auto_now=True)
    createdOn = models.DateTimeField("Created On", auto_now_add=True)
    description = models.CharField(max_length=500, blank=True)
    end_datetime = models.DateTimeField("End Date", blank=False)
    start_datetime = models.DateTimeField("Start Date", blank=False)
    capacity = models.IntegerField("Tour Capacity", blank=False)
    cost = models.DecimalField("Tour Cost", max_digits=7, decimal_places=2)
    title = models.CharField("Tour Title", max_length=60)

    def __str__(self):
        """
        Return a human readable representation of the tour instance.
        """
        return "title: {}, cost:{}, capacity:{}, start date:{}, end date:{} ".format(
            self.title,
            self.cost,
            self.capacity,
            self.start_datetime,
            self.end_datetime,
            )