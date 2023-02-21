from django.db import models
from offers.models import Location


class Company(models.Model):

    name = models.CharField(max_length=300)
    review = models.FloatField()
    reviews_count = models.IntegerField(default=0)
    # this should be array
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # offers count
    offers = models.IntegerField()
    # if more than one offers exist this should be an array
    offers_id = models.IntegerField()
