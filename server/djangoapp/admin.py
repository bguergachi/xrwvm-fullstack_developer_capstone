from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 4

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'car_make', 
        'type', 
        'year', 
        'color', 
        'price', 
        'horsepower', 
        'fuel_type', 
        'transmission'
    ]
    search_fields = ['name', 'dealer_id']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = [
        'name', 
        'description', 
        'headquarters', 
        'website', 
        'country_of_origin', 
        'established_year'
    ]
    search_fields = ['name']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
