from django.core import validators
from rest_framework import serializers

from core.models import CarModel, AutoParkModel


class CarRetriaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(validators=[
        validators.RegexValidator('^[a-z-A-Z]{2,20}$', 'brand only alpha'),
    ])

    class Meta:
        model = CarModel
        fields = '__all__'
        extra_kwargs = {
            'autopark': {'write_only': True}
        }


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'
