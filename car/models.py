from django.db import models


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Машину'
        verbose_name_plural = 'Машины'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.model

    def __repr__(self):
        return self.model
