from django.db import models


# Create your models here.

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    autopark = models.ForeignKey('AutoParkModel', on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'autopark'
    name = models.CharField(max_length=20)
