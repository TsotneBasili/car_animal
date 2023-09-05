from . models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'car_class', 'manufacture_year', 'price']



