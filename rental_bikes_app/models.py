from django.db import models

# Create your models here.


class Bike(models.Model):
    CITY_BIKE = 'CB'
    E_BIKE = 'EB'
    MOUNTAIN_BIKE = 'MB'
    ROAD_BIKE = 'RB'
    BIKE_TYPE_CHOICES = [
        (CITY_BIKE, 'City Bike'),
        (E_BIKE, 'E-Bike'),
        (MOUNTAIN_BIKE, 'Mountain Bike'),
        (ROAD_BIKE, 'Road Bike'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='bike_images')
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    bike_type = models.CharField(max_length=2, choices=BIKE_TYPE_CHOICES, default=CITY_BIKE)
    def __str__(self):
        return self.name

class Customer(models.Model):
    email = models.EmailField(unique=True)
    user_name = models.CharField(unique=True,max_length=35,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.email

    def reserved_bikes(self):
        return Bike.objects.filter(rental__user=self)

class Rental(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rental_day = models.DateField()

class DamageReport(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    damage_description = models.TextField()
    damage_location = models.CharField(max_length=255)
    report_time = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Damage Report for Bike {self.bike.name} by User {self.user.user_name}"