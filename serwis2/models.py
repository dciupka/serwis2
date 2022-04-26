from django.db import models


class Geoinfo(models.Model):
    _type = models.CharField(max_length=200)
    _id = models.IntegerField()
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


