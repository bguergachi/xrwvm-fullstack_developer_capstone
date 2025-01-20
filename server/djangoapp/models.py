from django.db import models
from django.utils.timezone import now
from django.core import validators


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    headquarters = models.CharField(max_length=100)
    website = models.URLField()
    country_of_origin = models.CharField(max_length=100)
    established_year = models.IntegerField(
        validators=[
            validators.MaxValueValidator(now().year),
            validators.MinValueValidator(1800)
        ]
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default='SUV'
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            validators.MaxValueValidator(2023),
            validators.MinValueValidator(2015)
        ]
    )
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    horsepower = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)

    def __str__(self):
        return self.name
