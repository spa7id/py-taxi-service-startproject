from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
