from django.contrib import admin
from .models import CarModel


# Register your models here.
# admin.site.register(CarModel)
@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'year', 'price')
