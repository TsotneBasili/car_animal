from . models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'group', 'herbivores']
