from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=70)
    lng = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=60, default="")
    location_description = models.CharField(max_length=300)
    city = models.CharField(max_length=50, default="Beirut", null=False)
    review = models.FloatField()
    reviews_count = models.IntegerField(default=0)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
