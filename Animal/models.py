from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    herbivores = models.BooleanField()
