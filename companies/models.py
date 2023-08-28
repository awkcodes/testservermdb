from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=300)
    review = models.FloatField()
    reviews_count = models.IntegerField(default=0)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
