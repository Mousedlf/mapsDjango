from django.db import models

# Create your models here.

class SavedPlace(models.Model):
    label = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=400)
    latitude = models.FloatField()
    longitude = models.FloatField()
