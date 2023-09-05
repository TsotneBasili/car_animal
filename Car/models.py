from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    car_class = models.CharField(max_length=100)
    manufacture_year = models.IntegerField()
    price = models.IntegerField()
