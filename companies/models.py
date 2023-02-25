from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=300)
    review = models.FloatField()
    reviews_count = models.IntegerField(default=0)
    # this should be array
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
