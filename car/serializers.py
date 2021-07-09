from django.core import validators
from rest_framework import serializers

from .models import CarModel, AutoParkModel

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

    def validate_year(self, year):
        if year % 2 == 0:
            raise serializers.ValidationError('only odd years')
        return year

    def validate(self, all_fields):
        print(all_fields)
        return all_fields


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'
