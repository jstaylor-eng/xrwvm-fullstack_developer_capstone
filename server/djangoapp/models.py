from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # country = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # ('Hatchback', 'Hatchback'),
        # ('Van', 'Van'),
    ]
    type = models.CharField(max_length=30, choices=CAR_TYPES, default='Sedan')
    year = models.IntegerField(default=2024,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2025)
        ])
    # colour = models.CharField(max_length=100)
    # secondhand = models.BooleanField(default=False)
    def __str__(self):
        return self.name
